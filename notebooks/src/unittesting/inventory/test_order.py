""" Test cases for the Order class.
"""
import unittest

from order import Order
from warehouse import Warehouse


class TestOrder(unittest.TestCase):
    """Test the Order class.
    """

    def setUp(self) -> None:
        """Create a warehouse with 10 shoes, 2 hats, and 0 umbrellas
        """
        self.wh = Warehouse({'shoes': 10, 'hats': 2, 'umbrellas': 0})

    def test_order_in_stock(self) -> None:
        """Test that an order for an item in stock is successful.
        """
        # Create an order for 1 hat
        status, item, quantity = Order.create_order(self.wh, 'hats', 1)
        self.assertEqual(status, 'ok')
        self.assertEqual(item, 'hats')
        self.assertEqual(quantity, 1)
        self.assertEqual(self.wh.stock_count('hats'), 1)

    def test_order_not_in_stock(self) -> None:
        """Test that an order for an item not in stock is unsuccessful.
        """
        # Create an order for 1 umbrella
        status, item, quantity = Order.create_order(self.wh, 'umbrellas', 1)
        self.assertEqual(status, 'not available')
        self.assertEqual(item, 'umbrellas')
        self.assertEqual(quantity, 1)
        self.assertEqual(self.wh.stock_count('umbrellas'), 0)

    def test_order_unknown_item(self) -> None:
        """Test that an order for an unknown item is unsuccessful.
        """
        # Create an order for 1 sock
        # There's no socks in the warehouse
        status, item, quantity = Order.create_order(self.wh, 'socks', 1)
        self.assertEqual(status, 'not available')
        self.assertEqual(item, 'socks')
        self.assertEqual(quantity, 1)
