""" Test the Order class using hypothesis to generate test cases.
    Tests fixed version of create_order method.
"""
import unittest
from hypothesis import given
import hypothesis.strategies as st
from order import Order
from warehouse import Warehouse


class TestOrder(unittest.TestCase):
    """
    Test the Order class.
    """

    def setUp(self) -> None:
        self.wh = Warehouse({'shoes': 10, 'hats': 2, 'umbrellas': 0})

    @given(item=st.sampled_from(['shoes', 'hats', 'umbrellas']),
           quantity=st.integers(min_value=1, max_value=100))
    def test_stock_level_plus_quantity_equals_initial_stock_level(
            self,
            item: str,
            quantity: int) -> None:
        """Test that the stock level plus the quantity
        equals the initial stock level.
        """
        initial_stock_level = self.wh.stock_count(item)
        print(f'{item=} = {initial_stock_level=}')
        status, item, quantity = Order.create_order_fixed(
            self.wh, item, quantity)
        if status == 'ok':
            self.assertEqual(self.wh.stock_count(item) +
                             quantity, initial_stock_level)
        elif status == 'not available':
            self.assertEqual(self.wh.stock_count(item), initial_stock_level)


if __name__ == '__main__':
    unittest.main(verbosity=2)
