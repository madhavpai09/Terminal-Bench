from fastapi import FastAPI
from api import task

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Terminal Bench API"}


app.include_router(task.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)    
