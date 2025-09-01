from urllib import response
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database_connection import get_db
from ..models import User
from ..schemas import ShowBalanceResponse

router = APIRouter(prefix="/wallet", tags=["wallet"])

@router.get("/{user_id}/balance", response_model=ShowBalanceResponse)
async def get_balance(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    return ShowBalanceResponse(user_id=user.id, balance=user.balance, last_updated=user.updated_at)

@router.post("/{user_id}/add-money")
async def add_money(user_id: int, amount: float, description: str, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    user.balance += amount
    db.commit()

    return {
        "transaction_id": 123,
        "user_id": user.id,
        "amount": amount,
        "new_balance": user.balance,
        "transaction_type": "CREDIT"
    }

@router.post("/{user_id}/withdraw")
async def withdraw_money(user_id: int, amount: float, description: str, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    if user.balance < amount:
        raise HTTPException(status_code=400, detail="Insufficient balance")

    user.balance -= amount
    db.commit()

    return {
        "transaction_id": 123,
        "user_id": user.id,
        "amount": amount,
        "new_balance": user.balance,
        "transaction_type": "DEBIT"
    }
