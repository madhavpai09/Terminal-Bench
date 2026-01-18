from fastapi import FastAPI
from api import task_api
from api import taskset_api
    
app = FastAPI()

@app.get("/")
def root():
    return {"message": "Terminal Bench API"}


app.include_router(task_api.router)
app.include_router(taskset_api.router)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)    
