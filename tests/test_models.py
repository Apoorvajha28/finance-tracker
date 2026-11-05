import pytest
from app.models import Transaction, Account


def test_high_value_true_for_large_amount():
    t = Transaction("2026-11-01", 500, "EUR", "Laptop", "Electronics")
    assert t.is_high_value() is True

def test_high_value_false_for_small_amount():
    t = Transaction("2026-11-01", 50, "EUR", "Lunch", "Food")
    assert t.is_high_value() is False

def test_negative_amount_is_rejected():
    with pytest.raises(ValueError):
        Transaction("2026-11-01", -10, "EUR", "Oops", "Food")

def test_empty_description_is_rejected():
    with pytest.raises(ValueError):
        Transaction("2026-11-01", 20, "EUR", "", "Food")

def test_account_total_adds_up():
    account = Account("Tester")
    account.add(Transaction("2026-11-01", 100, "EUR", "A", "Food"))
    account.add(Transaction("2026-11-01", 250, "EUR", "B", "Travel"))
    assert account.total() == 350

def test_account_high_value_filters():
    account = Account("Tester")
    account.add(Transaction("2026-11-01", 100, "EUR", "A", "Food"))
    account.add(Transaction("2026-11-01", 250, "EUR", "B", "Travel"))
    flagged = account.high_value()
    assert len(flagged) == 1
    assert flagged[0].description == "B"

