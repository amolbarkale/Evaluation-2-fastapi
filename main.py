from fastapi import FastAPI, HTTPException, status

app = FastAPI()

@app.get("/ping")
async def ping():
    return {"message": "pong"}