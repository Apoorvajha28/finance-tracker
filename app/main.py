from fastapi import FastAPI
from app.database import load_account
from app.rates import get_rate


app = FastAPI(title = "Finance Tracker API")

@app.get("/")
def home():
    return {"message": "Welcome to the Finance Tracker API"}


@app.get("/transactions")
def list_transactions():
    account = load_account("Apoorva")
    result = []
    for t in account.transactions:
        result.append({
            "date": t.date,
            "amount": t.amount,
            "currency": t.currency,
            "description": t.description,
            "category": t.category,
        })
    return result


@app.get("/summary")
def get_summary():
    account = load_account("Apoorva")
    return account.summary()



@app.get("/total-in/{currency}")
def total_in_(currency):
    account = load_account("Apoorva")
    rate = get_rate("EUR", currency.upper())
    total_eur = account.total()
    return {
        "total_eur": round(total_eur, 2),
        "currency": currency.upper(),
        "rate": rate,
        "converted_total": round(total_eur * rate, 2),
    }