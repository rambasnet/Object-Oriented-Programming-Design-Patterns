import unittest

from order import Order
from warehouse import Warehouse
from hypothesis import given
import hypothesis.strategies as st

class TestOrder(unittest.TestCase):
	def setUp(self):
		self.wh = Warehouse({'shoes': 10, 'hats': 2, 'umbrellas': 0})

	@given(item = st.sampled_from(['shoes', 'hats', 'umbrellas']),
		quantity = st.integers(min_value=1, max_value=4))
	def test_stock_level_plus_quantity_equals_initial_stock_level(self, item: str, quantity: int):
		initial_stock_level = self.wh.stock_count(item)
		print(f'{item=} = {initial_stock_level=}')
		status, item, quantity = Order.create_order_fixed(self.wh, item, quantity)
		if status == 'ok':
			self.assertEqual(self.wh.stock_count(item) + quantity, initial_stock_level)
		elif status == 'not available':
			self.assertEqual(self.wh.stock_count(item), initial_stock_level)

if __name__ == '__main__':
	unittest.main(verbosity=2)