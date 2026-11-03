import pytest
from fastapi.testclient import TestClient
from src.billing import app

client = TestClient(app)

def test_webhook_invalid_signature():
    response = client.post("/webhook", data=b"{}", headers={"stripe-signature": "invalid"})
    assert response.status_code == 400

def test_tier_mapping():
    # Verify that the tier mapping logic exists and is accessible
    from src.billing import TIER_MAP
    assert "price_standard_id" in TIER_MAP
    assert TIER_MAP["price_standard_id"] == "STANDARD"