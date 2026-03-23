from sqlalchemy.orm import Mapped,mapped_column
from app.database.base import Base

class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(autoincrement=True,primary_key=True)
    full_name:Mapped[str]
    email: Mapped[str]
    password: Mapped[str]
    phone_number: Mapped[str]