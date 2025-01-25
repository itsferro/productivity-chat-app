import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.utils.jwt import create_access_token

@pytest.fixture(scope="module")
def test_client():
    client = TestClient(app)
    yield client

@pytest.fixture
def auth_headers():
    user_data = {"sub": "testuser"}
    token = create_access_token(user_data)
    return {"Authorization": f"Bearer {token}"}

def test_send_message(test_client, auth_headers):
    response = test_client.post(
        "/messages/",
        headers=auth_headers,
        json={"conversation_id": 1, "content": "Hello!"}
    )
    assert response.status_code == 201
    data = response.json()
    assert data["content"] == "Hello!"

def test_retrieve_message_details(test_client, auth_headers):
    response = test_client.get("/messages/1", headers=auth_headers)
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1
    assert "content" in data

def test_edit_message(test_client, auth_headers):
    response = test_client.put(
        "/messages/1",
        headers=auth_headers,
        json={"content": "Updated content"}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["content"] == "Updated content"

def test_delete_message(test_client, auth_headers):
    response = test_client.delete("/messages/1", headers=auth_headers)
    assert response.status_code == 200
    data = response.json()
    assert data["message"] == "message deleted successfully"
