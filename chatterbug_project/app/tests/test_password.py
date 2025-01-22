import string
import pytest
from fastapi.testclient import TestClient
from fastapi_limiter import FastAPILimiter
from fastapi import FastAPI
import aioredis
from app.main import app as main_app
from app.services.password_services import generate_password


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

    result = generate_password(12, True, True)
    assert len(result) == 12
    assert any(char.isdigit() for char in result)
    assert any(char in string.punctuation for char in result)


def test_generate_password_invalid_length():
    # result = generate_password(11, True, True)
    # print("password is " + str(result))
    # print("length is " + str(len(str(result))))
    with pytest.raises(ValueError, match=".*Password length must be between 12 and 128.*"):
        generate_password(11, True, True)


def test_generate_password_no_character_type():
    with pytest.raises(ValueError, match=".*At least one character type must be selected.*"):
        generate_password(12, False, False)
