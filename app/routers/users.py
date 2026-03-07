from fastapi import APIRouter

users_router = APIRouter(prefix="/users", tags=["users"])

@users_router.get("/")
async def list():
  return ["Ana", "Carlos", "Lewis"]

@users_router.get("/{user_id}")
async def search(user_id: int):
  return {"id": user_id, "name": "Example"}