from pydantic import BaseModel
from typing import Optional

class TaskCreate(BaseModel):
    name: str
    description : Optional[str] = None
    complexity : Optional[str] = None
    priority : Optional[str] = None
    environment : Optional[str] = None

    
class TaskSetCreate(BaseModel):
    name: str
    description : Optional[str] = None
    tasks : list[TaskCreate]
