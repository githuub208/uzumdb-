from sqlalchemy.orm import Mapped,mapped_column,relationship
from app.database.base import Base
from typing import List
from datetime import datetime



class Category(Base):
    __tablename__ = "category"
    id: Mapped[int]  = mapped_column(autoincrement=True, primary_key=True)
    name: Mapped[str]
    description: Mapped[str]
    create_at: Mapped[datetime] =  mapped_column(default=datetime.now())

    product: Mapped[List["Product"]] = relationship(back_populates="category")

