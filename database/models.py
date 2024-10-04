from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

class Base(DeclarativeBase):
    pass

class Users(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key = True)
    email: Mapped[str] = mapped_column(String(50))
    priority_group_id: Mapped[int] = mapped_column(ForeignKey("priority_groups.id"))

    priority_groups: Mapped["PriorityGroups"] = relationship(back_populates = "users")

class PriorityGroups(Base):
    __tablename__ = "priority_groups"

    id: Mapped[int] = mapped_column(primary_key = True)
    priority: Mapped[int]

    users: Mapped["Users"] = relationship(back_populates = "priority_groups")

class Statuses(Base):
    __tablename__ = "statuses"

    id: Mapped[int] = mapped_column(primary_key = True)
    title: Mapped[str] = mapped_column(String(30))