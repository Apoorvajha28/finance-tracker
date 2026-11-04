# models.py
# This file holds the "building blocks" (classes) of our finance tracker.

class Transaction:
    def __init__(self, date, amount, currency, description, category ):
        if amount <= 0:
            raise ValueError(f"Amount must be positive, got {amount}")
        if not description:
            raise ValueError("Description cannot be empty")

        self.date = date
        self.amount = amount
        self.currency = currency
        self.description = description
        self.category = category

    def is_high_value(self, threshold = 200):
        return self.amount > threshold

    def __repr__(self):
        return f"Transaction({self.date}, {self.amount}, {self.currency}, {self.description}, {self.category}\n)"


class Account:
    def __init__(self, owner, currency = "EUR"):
        self.owner = owner
        self.currency = currency
        self.transactions = []

    def add(self, transaction):
        self.transactions.append(transaction)

    def total(self):
        result = 0
        for t in self.transactions:
            result += t.amount
        return result

    def high_value(self, treshold = 200):
        flagged = []
        for t in self.transactions:
            if t.is_high_value(treshold):
                flagged.append(t)
        return flagged

    def __repr__(self):
        return f"Account({self.owner}, {len(self.transactions)} transactions, total {self.total()} {self.currency})"


if __name__ == "__main__":
    account = Account("Apoorva")
    
    rows = [

        ("2026-11-02", 250, "EUR", "Flight ticket", "Travel"),
        ("2026-11-02", -12, "EUR", "Oops typo", "Food"),
        ("2026-11-03", 800, "EUR", "", "Electronics"),
        ("2026-11-03", 45, "EUR", "Groceries", "Food")
    ]

    for row in rows:
        date, amount, currency, description, category = row
        try:
            transaction = Transaction(date, amount, currency, description, category)
            account.add(transaction)
            print(f"Added transaction: {description}")
        except ValueError as error:
            print(f"Skipped transaction: {error}")

    print(f"\n{account}")
    print(f"\nTotal spent:{account.total()} EUR")




   
   