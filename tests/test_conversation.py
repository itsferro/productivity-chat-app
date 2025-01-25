import pytest
from fastapi.testclient import TestClient
from app.main import app  # Update with the actual path to your FastAPI app

@pytest.fixture(scope="module")
def test_client():
    client = TestClient(app)
    yield client


def test_retrieve_logged_in_user_conversations(test_client):
    response = test_client.get("/conversations/")
    assert response.status_code == 200
    data = response.json()
    assert "conversations" in data
    assert isinstance(data["conversations"], list)
    assert data["conversations"][0]["conversation_id"] == "1_2"


def test_retrieve_conversation_content(test_client):
    response = test_client.get("/conversations/5")
    assert response.status_code == 200
    data = response.json()
    assert data["conversation_id"] == 5
    assert "messages" in data
    assert len(data["messages"]) > 0
    assert data["messages"][0]["content"] == "Hello"


def test_retrieve_conversation_details(test_client):
    response = test_client.get("/conversations/1/details")
    assert response.status_code == 200
    data = response.json()
    assert data["conversation_id"] == 1
    assert "participants_ids" in data
    assert data["participants_ids"] == [1, 2]


def test_update_conversation_details(test_client):
    response = test_client.put("/conversations/1/details", json={
        "priority": 10,
        "tags": "updated tag",
        "labels": "updated label"
    })
    assert response.status_code == 200
    data = response.json()
    assert data["conversation_id"] == "1_2"
    assert data["priority"] == 5  # Verify the unchanged value
    assert data["tags"] == "some tag"  # Verify the returned value from the stub


def test_delete_conversation(test_client):
    response = test_client.delete("/conversations/1")
    assert response.status_code == 200
    data = response.json()
    assert data["message"] == "conversation deleted successfully"
