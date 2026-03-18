from fastapi import APIRouter,Depends,status,HTTPException
from sqlalchemy import select
from app.database.connection import get_db
from app.model.category import Category
from app.schema.category import ResponseCategory,CreateCategory,UpdateCategory
from typing import List

router = APIRouter(tags=["Category"],prefix="/category")

@router.get("/",response_model=List[ResponseCategory])
def get_category(category: str = None, db = Depends(get_db)):
    if category:
        query = select(Category).where(Category.name.like(f"%{category}%"))
    else:
        query = select(Category)

    return db.execute(query).scalars().all()

@router.post("/",status_code=status.HTTP_201_CREATED)
def create_category(data: CreateCategory, db = Depends(get_db)):
    obj = Category(
        name = data.name,
        description = data.description
    )
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

@router.put("/{category_id}")
def update_category(category_id: int, data:UpdateCategory,db = Depends(get_db)):
    category = db.get(Category,category_id)
    if not category:
        raise HTTPException(404,"Category not found")
    category.name = data.name
    category.description = data.description
    db.commit()
    db.refresh(category)
    return category

@router.delete("/{category_id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_category(category_id: int,db = Depends(get_db)):
    category = db.get(Category,category_id)
    if not category:
        raise  HTTPException(404,"Category not found")
    db.delete(category)
    db.commit()
