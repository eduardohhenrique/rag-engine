from fastapi import FastAPI
from app.routers import users, products

app = FastAPI() # uvicorn app.main:app --reload


app.include_router(users.users_router)
app.include_router(products.products_router)