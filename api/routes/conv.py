from fastapi import APIRouter
"""
"""


router = APIRouter(prefix="/conversations")


@router.get("/")
def retrieve_logged_in_user_conversations():
    return {
            "conversations": [
                {
                    "conversation_id": "1_2",
                    "participants_ids": [1, 2],
                    "participants_names": ["Feras", "Peninnah"],
                    "participants_nicknames": ["Feras", "Peninnah"],
                    "number_of_messages": 5,
                    "priority": 5,
                    "tags": "some tag",
                    "labels": "some label"
                    }
                ]
            }


@router.get("/{id}")
def retrieve_conversation_content():
    return {
            "conversation_id": 5,
            "participants": [1, 2],
            "messages": [
                {
                    "message_id": 99,
                    "sender_id": 1,
                    "recipient_id": 2,
                    "content": "Hello",
                    "timestamp": "2024-01-02T14:20:00Z",
                    "status": "delivered"
                    },
                {
                    "message_id": 100,
                    "sender_id": 2,
                    "recipient_id": 1,
                    "content": "Hey! All good?",
                    "timestamp": "2024-01-02T14:21:00Z",
                    "status": "read"
                    }
                ]
            }


@router.get("/{id}/details")
def retrieve_conversation_details():
    return {
            "conversation_id": 1,
            "participants_ids": [1, 2],
            "participants_names": ["Feras", "Peninnah"],
            "number_of_messages": 5
            }


@router.put("/{id}/details")
def update_conversation_details():
    return {
            "conversation_id": "1_2",
            "participants_ids": [1, 2],
            "participants_names": ["Feras", "Peninnah"],
            "participants_nicknames": ["Feras", "Peninnah"],
            "number_of_messages": 5,
            "priority": 5,
            "tags": "some tag",
            "labels": "some label"
            }


@router.delete("/{id}")
def delete_conversation():
    return {
            "message": "conversation deleted successfully"
            }
