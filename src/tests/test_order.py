# src/tests/test_order.py

from pos.order import LineItem, Order

def test_empty_order_total() -> None:
    order = Order()
    assert order.total == 0


def test_order_total() -> None:
    order = Order()
    order.line_items.append(LineItem(name="Test", price=1000))
    assert order.total == 1000

    