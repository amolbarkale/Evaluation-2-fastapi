from email.policy import HTTP
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from .. import schemas
from .. import models
from .. import database_connection

get_db = database_connection.get_db

router = APIRouter(prefix="/transfers", tags=["transfers"])

@router.post("/")
async def create_transfer(transfer: schemas.TransferCreate, db: Session = Depends(get_db)):
    sender = db.query(models.User).filter(models.User.id == transfer.sender_user_id).first()
    recipient = db.query(models.User).filter(models.User.id == transfer.recipient_user_id).first()

    if not sender or not recipient:
        raise HTTPException(status_code=404, detail="Sender or recipient not found")

    if sender.balance < transfer.amount:
        raise HTTPException(
            status_code=400,
            detail={
                "error": "Insufficient balance",
                "current_balance": sender.balance,
                "required_amount": transfer.amount
            }
        )

    # Deduct from sender and add to recipient
    sender.balance -= transfer.amount
    recipient.balance += transfer.amount

    # Create transfer record
    db_transfer = models.Transfers(
        sender_user_id=transfer.sender_user_id,
        recipient_user_id=transfer.recipient_user_id,
        amount=transfer.amount,
        description=transfer.description
    )
    db.add(db_transfer)

    # Create transaction records
    sender_transaction = models.Transactions(
        user_id=transfer.sender_user_id,
        transaction_type="TRANSFER_OUT",
        amount=transfer.amount,
        description=transfer.description,
        reference_transaction_id=db_transfer.id,
        recipient_user_id=transfer.recipient_user_id
    )
    recipient_transaction = models.Transactions(
        user_id=transfer.recipient_user_id,
        transaction_type="TRANSFER_IN",
        amount=transfer.amount,
        description=transfer.description,
        reference_transaction_id=db_transfer.id,
        recipient_user_id=transfer.sender_user_id
    )

    db.add(sender_transaction)
    db.add(recipient_transaction)

    db.commit()
    db.refresh(db_transfer)

    return {
        "transfer_id": db_transfer.id,
        "sender_transaction_id": sender_transaction.id,
        "recipient_transaction_id": recipient_transaction.id,
        "amount": transfer.amount,
        "sender_new_balance": sender.balance,
        "recipient_new_balance": recipient.balance,
        "status": "completed"
    }


@router.get("/{transfer_id}")
async def get_transfer(transfer_id: str, db: Session = Depends(get_db)):
    transfer = db.query(models.Transfers).filter(models.Transfers.id == transfer_id).first()
    if not transfer:
        raise HTTPException(status_code=404, detail="Transfer not found")
    return transfer