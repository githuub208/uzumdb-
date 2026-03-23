from pydantic import BaseModel,EmailStr,Field

class CreateUser(BaseModel):
    full_name:str
    email: EmailStr
    password:str 
    phone_number:str

class UpdateUser(CreateUser):
    pass

class ResponseUser(CreateUser):
    id:int