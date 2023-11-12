# pos/payment.py

from typing import Protocol

from pos.card import CreditCard
from pos.order import Order


class PaymentProcessor(Protocol):
    def charge(self, card: CreditCard, amount: int) -> None:
        """Charge the credit card."""


def pay_order(order: Order, payment_processor: PaymentProcessor, card: CreditCard) -> None:
    if order.total == 0:
        raise ValueError("Can't pay an order with total is 0.")

    payment_processor.charge(card, amount=order.total)
    order.pay()
