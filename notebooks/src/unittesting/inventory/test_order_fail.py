"""
stock cannot appear and disappear across our transaction
if we take some items from the warehouse, the number we took plus
the number we have left should equal the number we started with in the
warehouse in the following test we run our test with the item parameter chosen
raondomly from 'hat' or 'shoe' and the quantity chosen from 1 to 4
"""

import unittest
from order import Order
from warehouse import Warehouse
from hypothesis import given
from hypothesis import settings, Phase
import hypothesis.strategies as st


class TestOrder(unittest.TestCase):
    """ Test the Order class"""

    def setUp(self) -> None:
        """ Create a warehouse with some initial stock
        """

        self.wh = Warehouse({'shoes': 10, 'hats': 5, 'umbrellas': 0})

    @given(
        item=st.sampled_from(['shoes', 'hats']),
        quant_request=st.integers(min_value=1, max_value=10)
    )
    @settings(max_examples=100, derandomize=True)  # ,
    # phases = [Phase.generate], database = None)
    def test_stock_level_plus_quantity_equals_initial_stock_level(
            self,
            item: str,
            quant_request: int) -> None:
        """Test that the stock level plus the quantity
            equals the initial stock level
        """

        stock_level = self.wh.stock_count(item)
        print(f'{item=}: {stock_level=} quant_reuest={quant_request}')
        status, item, quantity = Order.create_order(
            self.wh, item, quant_request)
        print(f'{status=} {item=} {quantity=}')
        new_stock = self.wh.stock_count(item)
        if status == 'ok':
            self.assertEqual(
                new_stock + quantity,
                stock_level)


if __name__ == '__main__':
    unittest.main()
