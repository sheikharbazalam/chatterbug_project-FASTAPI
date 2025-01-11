import string
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_generate_password_valid():
    response = client.post(
        "/generate-password", json={"length": 12, "include_special": True, "include_numbers": True})
    assert response.status_code == 200
    data = response.json()
    assert "password" in data
    assert len(data["password"]) == 12


def test_generate_password_invalid_length():
    response = client.post("/generate-password", json={"length": 5})
    assert response.status_code == 400
    assert response.json() == {
        "detail": "Password length should be at least 8 characters."}


def test_generate_password_without_special_chars():
    response = client.post("/generate-password",
                           json={"length": 10, "include_special": False})
    assert response.status_code == 200
    data = response.json()
    assert len(data["password"]) == 10
    assert any(c not in string.punctuation for c in data["password"])
