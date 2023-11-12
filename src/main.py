# pos/main.py

from pos.card import CreditCard
from pos.order import LineItem, Order
from pos.payment import pay_order
from pos.processor import PaymentProcessor
from pos.settings import get_settings


def read_card_info() -> CreditCard:
    card = input("Please enter your card number: ")
    month = int(input("Please enter the card expiry month: "))
    year = int(input("Please enter the card expiry year: "))
    return CreditCard(card, month, year)


def main():
    payment_processor = PaymentProcessor(get_settings().api_key)
    order = Order()
    order.line_items.append(LineItem(name="Pizza", price=2300, quantity=3))
    order.line_items.append(LineItem(name="Soda", price=325, quantity=6))

    card = read_card_info()
    pay_order(order, payment_processor, card)


if __name__ == "__main__":
    main()
