from fastapi import APIRouter, Depends
from core.database import get_db
from core.dependencies import get_current_user
from services.order_service import *

router = APIRouter(prefix="/orders", tags=["Orders"])

@router.post("/checkout")
def checkout(db = Depends(get_db),
             user = Depends(get_current_user)):

    return create_order_from_cart(db, str(user["_id"]))

@router.get("/")
def get_orders(db = Depends(get_db),
               user = Depends(get_current_user)):

    return get_user_orders(db, str(user["_id"]))

