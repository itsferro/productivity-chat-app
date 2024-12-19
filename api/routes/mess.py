from fastapi import APIRouter
"""
"""


router = APIRouter(prefix="/messages")


@router.post("/")
def send_message():
    return {
            "message_id": 101,
            "sender_id": 1,
            "recipient_id": 2,
            "content": "Hello, how are you?",
            "timestamp": "2024-01-02T14:22:00Z",
            "status": "sent"
            }


@router.get("/{id}")
def retrieve_message_details():
    return {
            "message_id": 101,
            "sender_id": 1,
            "recipient_id": 2,
            "content": "Hello, how are you?",                                                "timestamp": "2024-01-02T14:22:00Z",                                             "status": "sent"
            }


@router.put("/{id}")
def edit_message():
    return {
            "message_id": 101,
            "sender_id": 1,
            "recipient_id": 2,
            "content": "Hello, how are you?",
            "timestamp": "2024-01-02T14:22:00Z",
            "status": "sent"
            }


@router.delete("/{id}")
def delete_message():
    return {
            "message": "message deleted successfully"
            }
