from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_bitcoin_price():
    response = client.get("/bitcoin-price")
    assert response.status_code == 200
    data = response.json()
    assert "bitcoin_price_usd" in data
    assert isinstance(data["bitcoin_price_usd"], (float, int))
