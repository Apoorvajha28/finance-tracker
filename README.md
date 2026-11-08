# Finance Tracker

A personal finance tracker that imports transactions, categorises them, converts
currencies using live exchange rates, stores them in a database, and serves it all
through a small web API.

## What it does

- Imports transactions from a CSV file and skips any invalid rows
- Groups spending by category and flags high-value transactions
- Saves a summary report as JSON
- Converts totals to other currencies using live exchange rates
- Stores transactions in a SQLite database
- Serves everything through a FastAPI web app with interactive docs

## Topics covered

- **Object-Oriented Programming** – `Transaction` and `Account` classes
- **File processing** – reading CSV, writing JSON
- **Requests & external libraries** – live currency rates
- **Error handling & exceptions** – input validation, safe file and network handling
- **Testing** – automated tests with pytest
- **Virtual environments** – isolated setup with `requirements.txt`
- **Database integration** – SQLite storage
- **Web development** – a FastAPI web API

## Setup
Create and activate a virtual environment, then install the dependencies:

    python3 -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt

## How to run
1. Create and fill the database (reads the CSV, creates `data/finance.db`):

       python -m app.database

2. Start the web app:

       python -m uvicorn app.main:app

3. Open in your browser:
   - http://localhost:8000/ – welcome message
   - http://localhost:8000/transactions – all transactions
   - http://localhost:8000/summary – spending summary
   - http://localhost:8000/total-in/INR – total in another currency
   - http://localhost:8000/docs – interactive API documentation

## Running the tests

    python -m pytest -v

