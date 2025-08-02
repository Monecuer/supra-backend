# app/main.py
from fastapi import FastAPI
from app.routes import auth
from app.database import engine, Base
from fastapi.middleware.cors import CORSMiddleware


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # or "*" for all origins (not recommended for prod)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(auth.router)
