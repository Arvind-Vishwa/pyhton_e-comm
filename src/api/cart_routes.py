from fastapi import APIRouter, Depends
from src.core.database import get_db
from src.core.dependencies import get_current_user
from src.schemas.cart_schema import CartItemCreate, CartItemUpdate
from src.services.cart_service import *

router = APIRouter(prefix="/cart", tags=["Cart"])

@router.post("/add")
def add_item(data: CartItemCreate,
             db = Depends(get_db),
             user = Depends(get_current_user)):

    return add_to_cart(db, str(user["_id"]), data.product_id, data.quantity)


@router.delete("/remove/{product_id}")
def remove_item(product_id: str,
                db = Depends(get_db),
                user = Depends(get_current_user)):

    return remove_from_cart(db, str(user["_id"]), product_id)

@router.put("/update")
def update_item(data: CartItemUpdate,
                db = Depends(get_db),
                user = Depends(get_current_user)):

    return update_cart_item(db, str(user["_id"]), data.product_id, data.quantity)

@router.get("/")
def get_cart(db = Depends(get_db),
             user = Depends(get_current_user)):

    return get_user_cart(db, str(user["_id"]))

