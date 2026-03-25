import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_ping():
    response = client.get("/ping")
    assert response.status_code == 200
    assert response.json() == {"message": "pong"}

def test_create_user():
    response = client.post("/users/", json={"name": "TestUser", "email": "test@example.com"})
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "TestUser"
    assert data["email"] == "test@example.com"
    assert "id" in data

def test_get_users():
    response = client.get("/users/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)