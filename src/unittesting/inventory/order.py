from warehouse import Warehouse

class Order:
	@staticmethod
	def create_order(warehouse: 'Warehouse', item: str, quantity: int):
		if warehouse.in_stock(item):
			warehouse.take_from_stock(item, quantity)
			return ('ok', item, quantity)
		else:
			return ('not available', item, quantity)

	@staticmethod
	def create_order_fixed(warehouse: 'Warehouse', item: str, quantity: int):
		if warehouse.in_stock_fixed(item, quantity):
			warehouse.take_from_stock(item, quantity)
			return ('ok', item, quantity)
		else:
			return ('not available', item, quantity)
