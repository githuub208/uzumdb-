from sqlalchemy.orm import Mapped,mapped_column,relationship
from app.database.base import Base
from typing import List
from datetime import datetime
from sqlalchemy import ForeignKey



class Product(Base):
    __tablename__ = "product"
    id: Mapped[int] = mapped_column(autoincrement=True,primary_key=True)
    name: Mapped[str]
    price: Mapped[int]
    stock: Mapped[str]
    description: Mapped[str]
    create_at: Mapped[datetime] =  mapped_column(default=datetime.now())
    category_id: Mapped[int] = mapped_column(ForeignKey("category.id"))

    category: Mapped["Category"] = relationship(back_populates="product")
