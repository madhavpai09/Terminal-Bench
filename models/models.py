from pydantic import BaseModel
from typing import Optional

class TaskCreate(BaseModel):
    task_name: str
    description : Optional[str] = None