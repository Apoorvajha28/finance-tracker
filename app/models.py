# models.py
# This file holds the "building blocks" (classes) of our finance tracker.

class Transaction:
    def __init__(self, date, amount, currency, description, category ):
        self.date = date
        self.amount = amount
        self.currency = currency
        self.description = description
        self.category = category

    def is_high_value(self, threshold = 200):
        return self.amount > threshold

    def __repr__(self):
        return f"Transaction(date = {self.date}, amount = {self.amount}, currency = {self.currency}, description = {self.description}, category = {self.category}\n)"


if __name__ == "__main__":
    transaction = [
    Transaction("2026-11-01", 250, "EUR", "Flight ticket", "Travel"),
    Transaction("2026-11-02", 12, "EUR", "Coffee", "Food"),
    Transaction("2026-11-03", 800, "EUR", "Laptop", "Electronics"),
    Transaction("2026-11-03", 45, "EUR", "Groceries", "Food")
    ]

    print(f"You have {len(transaction)} transactions.\n")
    for t in transaction:
        if t.is_high_value():
            print(f"High value transaction: {t}")
        else:
            print(f"Regular transaction: {t}")

   
   