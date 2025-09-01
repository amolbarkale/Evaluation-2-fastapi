from pydantic import BaseModel
from datetime import datetime

class UserCreate(BaseModel):
    username: str
    email: str
    password: str
    phone_number: str

class UserRead(BaseModel):
    id: int
    username: str
    email: str
    phone_number: str
    balance: float
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True

class TransferCreate(BaseModel):
    sender_user_id: int
    recipient_user_id: int
    amount: float
    description: str

class TransferRead(BaseModel):
    id: int
    sender_user_id: int
    recipient_user_id: int
    amount: float
    description: str
    created_at: datetime

    class Config:
        from_attributes = True

class TransactionCreate(BaseModel):
    user_id: int
    transaction_type: str
    amount: float
    description: str
    reference_transaction_id: int
    recipient_user_id: int

class TransactionRead(BaseModel):
    id: int
    user_id: int
    transaction_type: str
    amount: float
    description: str
    reference_transaction_id: int
    recipient_user_id: int
    created_at: datetime

    class Config:
        from_attributes = True