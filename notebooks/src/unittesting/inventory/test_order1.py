# stock cannot appear and disappear across our transaction
# if we take some items from the warehouse, the number we took plus
# the number we have left should equal the number we started with in the warehouse
# in the following test we run our test with the item parameter chosen 
# raondomly from 'hat' or 'shoe' and the quantity chosen from 1 to 4

import unittest
from order import Order
from warehouse import Warehouse
from hypothesis import given
import hypothesis.strategies as st

class TestOrder(unittest.TestCase):
	def setUp(self):
		self.wh = Warehouse({'shoes': 10, 'hats': 3, 'umbrellas': 0})

	@given(item = st.sampled_from(['shoes', 'hats']), 
		quantity = st.integers(min_value=1, max_value=4))
	def test_stock_level_plus_quantity_equals_initial_stock_level(self, item, quantity):
		initial_stock_level = self.wh.stock_count(item)
		print(f'{item=} = {initial_stock_level=}')
		status, item, quantity = Order.create_order(self.wh, item, quantity)
		if status == 'ok':
			self.assertEqual(self.wh.stock_count(item) + quantity, initial_stock_level)

if __name__ == '__main__':
	unittest.main(verbosity=2)