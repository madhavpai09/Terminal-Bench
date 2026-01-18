from pydantic import BaseModel
from typing import Optional

class TaskCreate(BaseModel):
    name: str
    description : Optional[str] = None
    

class TaskSetCreate(BaseModel):
    name: str
    description : Optional[str] = None
    tasks : list[TaskCreate]
