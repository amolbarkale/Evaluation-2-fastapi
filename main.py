from fastapi import FastAPI

from .routers import users, wallet

from .database_connection import Base, engine
from .routers import transactions, transfers, users

app = FastAPI(title="Digital Wallet API Application")

Base.metadata.create_all(bind=engine)

app.include_router(transactions.router)
app.include_router(transfers.router)
app.include_router(users.router)
app.include_router(wallet.router)


@app.get("/ping")
async def ping():
    return {"message": "pong"}