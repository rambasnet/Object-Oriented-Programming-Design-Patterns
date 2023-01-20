class Warehouse:
	def __init__(self, stock:dict[str, int]):
		self.stock = stock

	def in_stock(self, item_name: str) -> bool:
		return (item_name in self.stock) and (self.stock[item_name] > 0)

	def take_from_stock(self, item_name: str, quantity: int) -> None:
		if quantity <= self.stock[item_name]:
			self.stock[item_name] -= quantity
		else:
			raise Exception(f'Oversold {item_name}')

	def stock_count(self, item_name: str) -> int:
		return self.stock[item_name]

	def in_stock_fixed(self, item_name: str, quantity: int) -> bool:
		return (item_name in self.stock) and (self.stock[item_name] >= quantity)
		
		