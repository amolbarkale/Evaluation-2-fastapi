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
    db_transfer = models.Transfers(
        sender_user_id=transfer.sender_user_id,
        recipient_user_id=transfer.recipient_user_id,
        amount=transfer.amount,
        description=transfer.description
    )
    if not db_transfer:
        raise HTTPException(status_code=400, detail="Insufficient balance")
    
    db.add(db_transfer)
    db.commit()
    db.refresh(db_transfer)
    return {"message": "Transfer created successfully", "transfer": db_transfer}


@router.get("/{transfer_id}")
async def get_transfer(transfer_id: str, db: Session = Depends(get_db)):
    transfer = db.query(models.Transfers).filter(models.Transfers.id == transfer_id).first()
    if not transfer:
        raise HTTPException(status_code=404, detail="Transfer not found")
    return transfer