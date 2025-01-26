from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import Optional
from datetime import datetime
from todoist_api_python.api import TodoistAPI
from api.db import get_db
from api.utils.jwt import get_current_user
from api.models.users import User
from api.models.messages import Message
from api.schemas.todoist import TaskCreate
"""
"""


router = APIRouter(
        prefix="/tasks",
        tags=['Tasks']
        )


@router.post("/", status_code=status.HTTP_201_CREATED)
def add_message_as_Todoist_task(
        new_task: TaskCreate,
        current_user: User = Depends(get_current_user),
        db: Session = Depends(get_db)
        ):
    """
    """
    if new_task.mess_id <= 0:
        raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail="message id can't be less than or equal to zero.",
                headers={"WWW-Authenticate": "Bearer"}
                )
    try:
        message = db.query(Message).filter(Message.id == new_task.mess_id).first()
    except Exception as e:
        print(e)
        raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Internal server error (probably there's no message with an id={new_task.mess_id})",
                headers={"WWW-Authenticate": "Bearer"}
                )
    if message:
        print(message)
        api = TodoistAPI(current_user.todoist_token)
        try:
            projects = api.get_projects()
            inbox_project_id = next(project.id for project in projects if project.name == "Inbox")
            #inbox = project[0].name
            print("*******************************")
            print(f"inbox_project_id = {inbox_project_id}")
            print("*******************************")
        except Exception as e:
            print(f"Todoist API error: {e}")
            raise HTTPException(
                    status_code=status.HTTP_502_BAD_GATEWAY,
                    detail="Failed to interact with the Todoist API. Please try again later."
                    )
        try:
            task = api.add_task(content=message.content, project_id=inbox_project_id)
            print(task)
        except Exception as e:
            print(f"Todoist API error: {e}")
            raise HTTPException(
                    status_code=status.HTTP_502_BAD_GATEWAY,
                    detail="Failed to interact with the Todoist API. Please try again later."
                    )
        message.todoist_task_url = task.url
        message.update(db)
        return {
                "message": "successfully added a task to your Todoist account",
                "task_details": {
                    "content": task.content,
                    "url": task.url
                    }
                }
    else:
        print(message)
        raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail=f"you're not the sender of this message, or either the message by id={mess_id} does not exist or you're not part of it is conversation",
                headers={"WWW-Authenticate": "Bearer"}
                )
