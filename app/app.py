from fastapi import FastAPI
from api.task import tasks

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Terminal Bench API"}

app.include_router(tasks.router)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)    
