from fastapi import APIRouter

users_router = APIRouter(prefix="/users", tags=["users"])

@users_router.get("/")
async def list_users():
  return ["Ana", "Carlos", "Lewis"]

@users_router.get("/{user_id}")
async def get_user_by_id(user_id: int):
  return {
    "id": user_id, 
    "name": "Ana",
    "email": "ana@gmail.com"
    }