from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import api_router
"""
"""


app = FastAPI(title="productivity chat app api")

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router)

@app.get("/")
def root():
    return {"message": "Welcome to our productivity chat app api!"}
