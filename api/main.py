from fastapi import FastAPI
from api.routes import api_router
"""
"""

app = FastAPI(title="productivity chat app api")
app.include_router(api_router)

@app.get("/")
def root():
    return {"message": "Welcome to our productivity chat app api!"}
