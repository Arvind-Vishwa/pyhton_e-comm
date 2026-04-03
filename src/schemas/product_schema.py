from pydantic import BaseModel, HttpUrl
from typing import Optional

class ProductCreate(BaseModel):
    title: str
    description: str
    price: float
    category: str
    image_url: Optional[HttpUrl]

class ProductUpdate(BaseModel):
    title: Optional[str]
    description: Optional[str]
    price: Optional[float]
    category: Optional[str]
    image_url: Optional[HttpUrl]