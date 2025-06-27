from fastapi import FastAPI
from fastapi import Request
from schemas import Transaction
from redis_client import r

app = FastAPI()

@app.get("/")
def ping():
    return {"message":"alive!"}

@app.post("/transactions")
def ingest(tx: Transaction):
    tx_dict = tx.model_dump()
    r.xadd("tx_ingest", tx_dict)
    return {"status": "accepted"}