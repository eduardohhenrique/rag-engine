from fastapi import APIRouter

products_router = APIRouter(prefix="/products", tags=["products"])

@products_router.get("/")
async def list_products():
  return ["1223", "2321"]

@products_router.get("/{product_id}")
async def get_product_by_id(product_id: int):
  return {
    "id": product_id, 
    "product": "example"
    }
