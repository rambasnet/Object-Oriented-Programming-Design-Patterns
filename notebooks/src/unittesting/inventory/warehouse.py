from __future__ import annotations

class Warehouse:
	def __init__(self, stock:dict[str, int]):
		self.stock = stock

	def in_stock(self, item_name: str) -> bool:
		# true if item_name is in stock and the quantity is greater than 0
    # is this correct implementation to check if item_name is in stock?
		return (item_name in self.stock) and (self.stock[item_name] > 0)

	def take_from_stock(self, item_name: str, quantity: int) -> None:
		# subtract quantity from stock[item_name]
		if quantity <= self.stock[item_name]:
			self.stock[item_name] -= quantity
		else:
			# raise an exception if quantity is greater than stock[item_name]
			raise Exception(f'Oversold {item_name}')

	def stock_count(self, item_name: str) -> int:
		return self.stock[item_name]

	def in_stock_fixed(self, item_name: str, quantity: int) -> bool:
		# true if item_name is in stock and the stock[item_name] is greater than quantity ordered
		return (item_name in self.stock) and (self.stock[item_name] >= quantity)
		
		