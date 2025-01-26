import pytest
from fastapi.testclient import TestClient
from api.main import app

@pytest.fixture(scope="module")
def client(session):
    with TestClient(app) as client:
        yield client

def test_retrieve_users(client):
    response = client.get("/users/")
    assert response.status_code == 200
    assert "users" in response.json()
    assert len(response.json()["users"]) > 0

def test_retrieve_user_profile(client):
    response = client.get("/users/1")
    assert response.status_code == 200
    assert response.json()["username"] == "testuser"

def test_update_user_profile(client):
    update_data = {"username": "updateduser", "email": "updateduser@example.com"}
    response = client.put("/users/1", json=update_data)
    assert response.status_code == 200
    assert response.json()["username"] == "updateduser"

def test_update_other_user_profile(client):
    response = client.put("/users/2", json={"username": "anotheruser"})
    assert response.status_code == 403
    assert response.json()["detail"] == "you're only allowed to edit your own profile, You are not allowed to edit another user's profile."

def test_delete_user(client):
    response = client.delete("/users/1")
    assert response.status_code == 200
    assert response.json()["message"] == "user deleted successfully"

def test_invalid_user_id(client):
    response = client.get("/users/0")
    assert response.status_code == 422
    assert response.json()["detail"] == "user id can't be less than or equal to zero."

def test_search_users(client):
    response = client.get("/users/?search=testuser")
    assert response.status_code == 200
    assert len(response.json()["users"]) > 0
    assert "testuser" in response.json()["users"][0]["username"]
