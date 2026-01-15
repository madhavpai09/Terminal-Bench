from fastapi import FastAPI
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from api.router import router
from core.Task_creator import TaskCreate, main as task_create_main
from cli.setup import run_task_logic
from pydantic import BaseModel

class TaskRun(BaseModel):
    task_name: str

app = FastAPI()
@app.get("/")
def root():
    return {"message": "Terminal Bench API"}

@app.post("/create/{task_name}")
def create_task(task_name: str):
    task_create = TaskCreate(task_name=task_name)
    task_create_main(task=task_create)
    return {"message": "Task created successfully"}
app.include_router(router)

@app.post("/run/{task_name}")
def run_task(task_name: str):
    output = run_task_logic(task_name)
    return {"message": "Task run finished", "output": output}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)    