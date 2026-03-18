from pydantic import BaseModel
from datetime import datetime

class ResponseProduct(BaseModel):
    id: int
    name: str
    price: int
    stock: str
    description: str
    create_at: datetime
    category_id: int

class CreateProduct(BaseModel):
    name: str
    price: int
    stock: str
    description: str
    category_id: int

class UpdateProduct(CreateProduct):
    pass