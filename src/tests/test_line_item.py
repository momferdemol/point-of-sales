# src/tests/test_line_item.py

from pos.order import LineItem


def test_line_item_total() -> None:
    line_item = LineItem(name="Test", price=1500)
    assert line_item.total == 1500


def test_line_item_total_quantity() -> None:
    line_item = LineItem(name="Test", price=1500, quantity=2)
    assert line_item.total == 3000
