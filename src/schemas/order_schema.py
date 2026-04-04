from pydantic import BaseModel


class OrderResponse(BaseModel):
    id: str
    items: list
    total_price: float