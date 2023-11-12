# src/tests/test_payment.py

from datetime import date
import pytest

from pos.card import CreditCard
from pos.order import LineItem, Order, OrderStatus
from pos.payment import pay_order

@pytest.fixture  # type: ignore
def card() -> CreditCard:
    year = date.today().year + 2
    return CreditCard("1249190007575069", 1, year)


class PaymentProcessorMock:
    def charge(self, card: CreditCard, amount: int) -> None:
        print(f"Charging card number {card.number} for ${amount/100:.2f}")


def test_pay_order(card: CreditCard) -> None:
    order = Order()
    order.line_items.append(LineItem(name="Test", price=1500, quantity=2))
    pay_order(order, PaymentProcessorMock(), card)
    assert order.status == OrderStatus.PAID


def test_pay_order_invalid(card: CreditCard) -> None:
    with pytest.raises(ValueError):  # type: ignore
        order = Order()
        pay_order(order, PaymentProcessorMock(), card)

