from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

class Base(DeclarativeBase):
    pass

class Statuses(Base):
    __tablename__ = "statuses"

    id: Mapped[int] = mapped_column(primary_key = True)
    title: Mapped[str] = mapped_column(String(30))