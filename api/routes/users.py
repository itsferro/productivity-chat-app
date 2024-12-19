from fastapi import APIRouter
"""
"""


router = APIRouter(prefix="/users")


@router.get("/")
def retrieve_users():
    return {
            "users": [
                {
                    "user_id": 1,
                    "username": "user123",
                    "email": "user123@example.com",
                    "created_at": "2024-01-02T12:00:00Z",
                    "phone": "+218943717245",
                    "todoist_token": "khugvjhfgjhvkjh",
                    "last_seen_online": "2024-01-02T12:00:00Z"
                    }
                ]
            }


@router.get("/{id}")
def retrieve_user_profile_detail():
    return {
            "user_id": 1,
            "username": "user123",
            "email": "user123@example.com",
            "created_at": "2024-01-02T12:00:00Z",
            "phone": "+218943717245",
            "todoist_token": "khugvjhfgjhvkjh",
            "last_seen_online": "2024-01-02T12:00:00Z",
            "conversations_count": 20,
            "banned_users": [
                {
                    "user_id": 1,
                    "banned_at": "2024-01-02T12:00:00Z"
                    },
                {
                    "user_id": 1,
                    "banned_at": "2024-01-02T12:00:00Z"
                    }
                ]
            }


@router.put("/{id}")
def update_user_profile_detail():
    return {"user_id": 1,
            "username": "user123",
            "email": "user123@example.com",
            "created_at": "2024-01-02T12:00:00Z",
            "phone": "+218943717245",
            "todoist_token": "khugvjhfgjhvkjh",
            "last_seen_online": "2024-01-02T12:00:00Z",
            "conversations_count": 20,
            "banned_users": [
                {
                    "user_id": 1,
                    "banned_at": "2024-01-02T12:00:00Z"
                    },
                {
                    "user_id": 1,
                    "banned_at": "2024-01-02T12:00:00Z"
                    }
                ]
            }


@router.get("/{id}/status")
def check_online_offline_status():
    return {
            "message": "offline",
            "last_seen": "2024-01-02T12:00:00Z"
            }


@router.delete("/{id}")
def delete_user():
     return {
             "message": "user deleted successfully"
             }


@router.post("/bans")
def user_bans_list_control():
    return {
            "message": "you successfully added user 6 to your 'benned users' list"
            }
