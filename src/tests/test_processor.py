# src/tests/test_processor.py

from datetime import date

import pytest
from pos.card import CreditCard
from pos.processor import PaymentProcessor, luhn_checksum
from pos.settings import get_settings

API_KEY = get_settings().api_key or ""
CC_YEAR = date.today().year + 2

@pytest.fixture  # type: ignore
def payment_processor() -> PaymentProcessor:
    return PaymentProcessor(API_KEY)

def test_invalid_api_key() -> None:
    with pytest.raises(ValueError):  # type: ignore
        card = CreditCard("1249190007575069", 1, CC_YEAR)
        PaymentProcessor("").charge(card, 100)

def test_card_number_valid_date(payment_processor: PaymentProcessor) -> None:
    card = CreditCard("1249190007575069", 12, CC_YEAR)
    assert payment_processor.validate_card(card)

def test_card_number_invalid_date(payment_processor: PaymentProcessor) -> None:
    card = CreditCard("1249190007575069", 9, 1980)
    assert not payment_processor.validate_card(card)

def test_card_number_valid_luhn() -> None:
    assert luhn_checksum("1249190007575069")

def test_card_number_invalid_luhn() -> None:
    assert not luhn_checksum("1249190007575068")

def test_charge_card_valid(payment_processor: PaymentProcessor) -> None:
    card = CreditCard("1249190007575069", 12, CC_YEAR)
    payment_processor.charge(card, 150)

def test_charge_card_invalid(payment_processor: PaymentProcessor) -> None:
    with pytest.raises(ValueError):  # type: ignore
        card = CreditCard("1249190007575068", 12, CC_YEAR)
        payment_processor.charge(card, 150)

