from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from .. import models, database_connection

router = APIRouter(prefix="/transactions", tags=["transactions"])

@router.get("/detail/{transaction_id}")
async def get_transaction_detail(transaction_id: int, db: Session = Depends(database_connection.get_db)):
    transaction = db.query(models.Transaction).filter(models.Transaction.id == transaction_id).first()
    if not transaction:
        raise HTTPException(status_code=404, detail="Transaction not found")
    return transaction
