from sqlalchemy import Integer, String, Float, TIMESTAMP, func, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime

from .database_connection import Base

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    username: Mapped[str] = mapped_column(..., String, unique=True, index=True)
    email: Mapped[str] = mapped_column(String, unique=True, index=True)
    password: Mapped[str] = mapped_column(..., String)
    phone_number: Mapped[str] = mapped_column(String)
    balance: Mapped[float] = mapped_column(Float, default=0.0)
    created_at: Mapped[datetime] = mapped_column(TIMESTAMP, default=func.now())
    updated_at: Mapped[datetime] = mapped_column(TIMESTAMP, default=func.now(), onupdate=func.now())
    

class Transfers(Base):
    __tablename__ = "transfers"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    sender_user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"))
    recipient_user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"))
    amount: Mapped[float] = mapped_column(..., Float)
    description: Mapped[str] = mapped_column(String)
    created_at: Mapped[datetime] = mapped_column(TIMESTAMP, default=func.now())

class Transactions(Base):
    __tablename__ = "transactions"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"))
    transaction_type: Mapped[str] = mapped_column(..., String(20))  # 'CREDIT', 'DEBIT', 'TRANSFER_IN', 'TRANSFER_OUT'
    amount: Mapped[float] = mapped_column(..., Float)
    description: Mapped[str] = mapped_column(String)
    reference_transaction_id: Mapped[int] = mapped_column(Integer)  # For linking transfer transactions
    recipient_user_id: Mapped[int] = mapped_column(Integer)  # For transfers
    created_at: Mapped[datetime] = mapped_column(TIMESTAMP, default=func.now())