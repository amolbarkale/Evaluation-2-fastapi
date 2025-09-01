from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
# from ..models import User
from ..database_connection import get_db
from ..schemas import UserCreate, UserRead

router = APIRouter(prefix="/users", tags=["users"])

# @router.post("/")
# async def create_user(user: UserCreate, db: Session = Depends(get_db)):
#     db_user = User(username=user.username, email=user.email, password=user.password, phone_number=user.phone_number, balance=0)
#     db.add(db_user)
#     db.commit()
#     db.refresh(db_user)
#     return db_user

# @router.get("/{user_id}", response_model=UserRead)
# async def read_user(user_id: int, db: Session = Depends(get_db)):
#     user = db.query(User).filter(User.id == user_id).first()
#     if not user:
#         raise HTTPException(status_code=404, detail="User not found")
#     return user
