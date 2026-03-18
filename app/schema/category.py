from pydantic import BaseModel
from datetime import datetime

class ResponseCategory(BaseModel):
    id: int
    name: str
    description: str
    create_at: datetime

class CreateCategory(BaseModel):
    name: str
    description:str

class UpdateCategory(CreateCategory):
    pass