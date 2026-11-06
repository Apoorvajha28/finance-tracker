import sqlite3
from app.models import Transaction, Account

DB_FILE = "data/finance.db"


def setup():
    connection = sqlite3.connect(DB_FILE)
    with connection:
        connection.execute(
            """CREATE TABLE IF NOT EXISTS transactions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                date TEXT,
                amount REAL,
                currency TEXT,
                description TEXT,
                category TEXT)"""
        )
    connection.close()


def save_account(account):
    connection = sqlite3.connect(DB_FILE)
    with connection:
        connection.execute("DELETE FROM transactions")  # Clear existing data
        for t in account.transactions:
            connection.execute(
                "INSERT INTO transactions (date, amount, currency, description, category)"
                "VALUES (?, ?, ?, ?, ?)",
                (t.date, t.amount, t.currency, t.description, t.category),
            )
    connection.close()
    print(f"Saved {len(account.transactions)} transactions to {DB_FILE}")


def load_account(owner):
    account = Account(owner)
    connection = sqlite3.connect(DB_FILE)
    rows = connection.execute("SELECT date, amount, currency, description, category FROM transactions").fetchall()
    connection.close()
    for row in rows:
        date, amount, currency, description, category = row
        account.add(Transaction(date, amount, currency, description, category))
        return account


if __name__ == "__main__":
    setup()                        # make sure the table exists

    source = Account("Apoorva")    # load from CSV, save into the database
    source.load_csv("data/transactions.csv")
    save_account(source)

    loaded = load_account("Apoorva")   # load from the database

    print(f"Loaded back from database: {loaded}")
    print(f"Total from database: {loaded.total(): .2f} EUR")

