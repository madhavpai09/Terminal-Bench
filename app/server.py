import sys
import os
from fastapi import FastAPI

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if base_dir not in sys.path:
    sys.path.append(base_dir)

from app.api import task_api
from app.api import taskset_api
    
app = FastAPI()

@app.get("/")
def root():
    return {"message": "Terminal Bench API"}


app.include_router(task_api.router)
app.include_router(taskset_api.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.server:app", host="127.0.0.1", port=8000, reload=True)    
