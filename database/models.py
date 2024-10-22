from datetime import datetime, date
from typing import List
from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


class Users(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(50))
    priority_group_id: Mapped[int] = mapped_column(ForeignKey("priority_groups.id"))
    notifications: Mapped[bool]
    role: Mapped[str] = mapped_column(String(30), default="user")

    priority_groups: Mapped["PriorityGroups"] = relationship(back_populates="users")
    reservations: Mapped[List["Reservations"]] = relationship(back_populates="users", cascade="all, delete-orphan")


class PriorityGroups(Base):
    __tablename__ = "priority_groups"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(30))
    priority: Mapped[int] = mapped_column(nullable=True)

    users: Mapped[List["Users"]] = relationship(back_populates="priority_groups")


class Reservations(Base):
    __tablename__ = "reservations"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    created_at: Mapped[datetime]

    users: Mapped["Users"] = relationship(back_populates="reservations")
    reservations_dates: Mapped[List["ReservationsDates"]] = relationship(back_populates="reservations", cascade="all, delete-orphan")


class ReservationsDates(Base):
    __tablename__ = "reservations_dates"

    id: Mapped[int] = mapped_column(primary_key=True)
    reservation_id: Mapped[int] = mapped_column(ForeignKey("reservations.id"))
    date_of_reservation: Mapped[date]
    status_id: Mapped[int] = mapped_column(ForeignKey("statuses.id"))

    statuses: Mapped["Statuses"] = relationship(back_populates="reservations_dates")
    reservations: Mapped["Reservations"] = relationship(back_populates="reservations_dates")


class Statuses(Base):
    __tablename__ = "statuses"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(30))

    reservations_dates: Mapped[List["ReservationsDates"]] = relationship(back_populates="statuses")


class Config(Base):
    __tablename__ = "config"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    value: Mapped[str]
