from typing import List
from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import select
from app.database.connection import get_db
from app.model.user import  User
from app.schema.user import ResponseUser, CreateUser
from app.utils.security import  hashed_password

router = APIRouter(tags=["User"],prefix="/user")

@router.get("/",response_model=List[ResponseUser])
def get_user(db: Session = Depends(get_db)):
    return db.execute(select(User)).scalars().all()

@router.post("/sign_up",response_model=ResponseUser)
def sign_up(data:CreateUser,db: Session = Depends(get_db)):
    email = db.execute(select(User).where(User.email == data.email)).scalars().first()
    if  email:
        raise HTTPException(404,"EMAIL ALREADY EXISTS")
    obj = User(
        full_name = data.full_name,
        email = data.email,
        password = hashed_password(data.password),
        phone_number = data.phone_number
    )
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

# git add .
# git commit -m "first commit"
#  git push -u origin main