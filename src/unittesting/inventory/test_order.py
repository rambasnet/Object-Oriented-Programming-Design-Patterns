import unittest

from order import Order
from warehouse import Warehouse

class TestOrder(unittest.TestCase):
	def setUp(self):
		self.wh = Warehouse({'shoes': 10, 'hats': 2, 'umbrellas': 0})

	def test_order_in_stock(self):
		status, item, quantity = Order.create_order(self.wh, 'hats', 1)
		self.assertEqual(status, 'ok')
		self.assertEqual(item, 'hats')
		self.assertEqual(quantity, 1)
		self.assertEqual(self.wh.stock_count('hats'), 1)

	def test_order_not_in_stock(self):
		status, item, quantity = Order.create_order(self.wh, 'umbrellas', 1)
		self.assertEqual(status, 'not available')
		self.assertEqual(item, 'umbrellas')
		self.assertEqual(quantity, 1)
		self.assertEqual(self.wh.stock_count('umbrellas'), 0)

	def test_order_unknown_item(self):
		status, item, quantity = Order.create_order(self.wh, 'socks', 1)
		self.assertEqual(status, 'not available')
		self.assertEqual(item, 'socks')
		self.assertEqual(quantity, 1)
		

if __name__ == '__main__':
	unittest.main(verbosity=2)
	
