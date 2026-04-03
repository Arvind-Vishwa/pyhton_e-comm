from pydantic import BaseModel


class CartItemCreate(BaseModel):
    product_id: str
    quantity: int


class CartItemUpdate(BaseModel):
    product_id: str
    quantity: int