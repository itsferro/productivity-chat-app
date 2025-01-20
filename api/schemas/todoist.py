from datetime import datetime
from pydantic import BaseModel
from typing import Optional
"""
"""


class TaskCreate(BaseModel):
    """
    """
    mess_id: int
    gtd_app: str = "Todoist"
