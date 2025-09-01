from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from . import models
from .routers import transactions, transfers, users

app = FastAPI(title="Digital Wallet API Application")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

models.Base.metadata.create_all(bind=models.engine)

app.include_router(transactions.router)
app.include_router(transfers.router)
app.include_router(users.router)

@app.get("/ping")
async def ping():
    return {"message": "pong"}