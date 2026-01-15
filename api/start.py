from fastapi import FastAPI
import sys
sys.path.append("../api")
from router import router

app = FastAPI()
@app.get("/")
def root():
    return {"message": "Terminal Bench API"}

app.include_router(router)
