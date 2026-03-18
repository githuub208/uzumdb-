from fastapi import APIRouter,Depends,HTTPException,status
from sqlalchemy import select
from sqlalchemy.orm import selectinload
from app.database.connection import get_db
from app.model.product import Product
from app.schema.product import ResponseProduct,CreateProduct,UpdateProduct
from fastapi_pagination.ext.sqlalchemy import  paginate
from fastapi_pagination import Page, Params
router = APIRouter(tags=["Product"],prefix="/product")

@router.get("/",response_model=Page[ResponseProduct])
def get_product(product: str = None,params: Params = Depends(), db = Depends(get_db)):
    if product:
        query = (select(Product).options(selectinload(Product.category)).
                 where(Product.name.like(f"%{product}%")))
    else:
        query = (select(Product).options(selectinload(Product.category)))

    return paginate(db, query)

@router.post("/",status_code=status.HTTP_201_CREATED)
def create_product(data:CreateProduct,db = Depends(get_db)):
    obj = Product(
        name = data.name,
        price = data.price,
        stock = data.stock,
        description = data.description,
        category_id = data.category_id
    )
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

@router.put("/{product_id}")
def update_product(product_id: int, data: UpdateProduct,db = Depends(get_db)):
    product = db.get(Product,product_id)
    if not product:
        raise HTTPException(404,"Product not found")
    product.name = data.name
    product.price = data.price
    product.stock = data.stock
    product.description = data.description
    product.category_id = data.category_id
    db.commit()
    db.refresh(product)
    return product

@router.delete("/{product_id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_product(product_id:int,db = Depends(get_db)):
    product = db.get(Product,product_id)
    if not product:
        raise HTTPException(404,"product not found")
    db.delete(product)
    db.commit()