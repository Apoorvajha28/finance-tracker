# models.py
# This file holds the "building blocks" (classes) of our finance tracker.
# First up: a Transaction class. Type it in just below. 👇

class Transaction:
    def __init__(self, date, amount, currency, description, category ):
        self.date = date
        self.amount = amount
        self.currency = currency
        self.description = description
        self.category = category

    def is_high_value(self, threshold = 200):
        return self.amount > threshold


if __name__ == "__main__":
    # Let's create a transaction and see if it's high value.
    t = Transaction("2026-11-01", 250, "EUR", "Flight ticket", "Travel")
    print("Amount:", t.amount, t.currency) # Should print: Amount: 250 EUR
    print("Description:", t.description) # Should print: Description: Flight ticket
    print("High Value?", t.is_high_value())  # Should print True