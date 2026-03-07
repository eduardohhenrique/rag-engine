from fastapi import FastAPI

app = FastAPI() # uvicorn app.main:app --reload

from app.routers import users
app.include_router(users.users_router)