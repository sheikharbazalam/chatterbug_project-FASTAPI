import pytest
from fastapi.testclient import TestClient
from fastapi_limiter import FastAPILimiter
from fastapi import FastAPI
import aioredis
from app.main import app as main_app  # Import your main FastAPI app


# Fixture to initialize FastAPILimiter during test startup
@pytest.fixture(scope="session", autouse=True)
async def init_limiter():
    # Create a new FastAPI app for testing
    app = FastAPI()

    # Initialize Redis for rate limiting
    redis = await aioredis.from_url("redis://localhost", encoding="utf-8", decode_responses=True)

    # Initialize FastAPILimiter for the test app
    await FastAPILimiter.init(redis)
    yield
    await redis.close()

# Setup the test client using the app with FastAPILimiter initialized
client = TestClient(main_app)

# Test Case 1: Valid password generation


def test_generate_password_valid():
    payload = {
        "length": 16,
        "include_uppercase": True,
        "include_numbers": True,
        "include_special": True,
        "include_lowercase": True
    }
    response = client.post("/generate-password", json=payload)

    assert response.status_code == 200
    data = response.json()
    assert "password" in data
    assert len(data["password"]) == 16  # Should match requested length
    assert "length" in data
    assert isinstance(data["password"], str)

# Test Case 2: Password length too short


def test_generate_password_invalid_length():
    payload = {"length": 5}  # Invalid length
    response = client.post("/generate-password", json=payload)

    assert response.status_code == 400
    data = response.json()
    assert "detail" in data
    assert data["detail"] == "Password length must be at least 12 characters."

# Test Case 3: No character type selected


def test_generate_password_no_character_type():
    payload = {
        "length": 16,
        "include_uppercase": False,
        "include_numbers": False,
        "include_special": False,
        "include_lowercase": False
    }
    response = client.post("/generate-password", json=payload)

    assert response.status_code == 400
    data = response.json()
    assert "detail" in data
    assert data["detail"] == "At least one type of character must be included."

# Test Case 4: Rate Limiting (50 requests in 60 seconds)


def test_generate_password_rate_limited():
    payload = {"length": 16}

    for _ in range(50):
        response = client.post("/generate-password", json=payload)
        assert response.status_code == 200

    # 51st request should be rate-limited
    response = client.post("/generate-password", json=payload)
    assert response.status_code == 429  # Rate limit exceeded
