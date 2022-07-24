import pytest
from order import Order


def test_check_empty_order():
    order = Order()
    assert len(order.line_items) == 0
    