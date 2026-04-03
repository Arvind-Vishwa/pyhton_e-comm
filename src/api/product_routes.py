from fastapi import APIRouter, HTTPException, Depends
from src.schemas.product_schema import ProductCreate, ProductUpdate
from src.services.product_service import (
    create_product, get_products, get_product,
    update_product, delete_product
)
from src.core.dependencies import get_current_user

router = APIRouter()

# Create product (protected)
@router.post("/")
def create(data: ProductCreate, user=Depends(get_current_user)):
    product_id = create_product(data)
    return {"id": product_id}


# Get all products
@router.get("/")
def get_all(search: str = None, category: str = None, sort: str = None, page: int = 1, limit: int = 10):
    return get_products(search, category, sort, page, limit)


# Get single product
@router.get("/{product_id}")
def get_one(product_id: str):
    product = get_product(product_id)

    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    return product


# Update product (protected)
@router.put("/{product_id}")
def update(product_id: str, data: ProductUpdate, user=Depends(get_current_user)):
    updated = update_product(product_id, data)

    if not updated:
        raise HTTPException(status_code=404, detail="Product not found")

    return updated


# Delete product (protected)
@router.delete("/{product_id}")
def delete(product_id: str, user=Depends(get_current_user)):
    success = delete_product(product_id)

    if not success:
        raise HTTPException(status_code=404, detail="Product not found")

    return {"message": "Deleted successfully"}