"""Order class for the inventory system
"""
from __future__ import annotations
from warehouse import Warehouse


class Order:
    """Order class to create orders for the warehouse.
    """
    @staticmethod
    def create_order(warehouse: 'Warehouse',
                     item: str,
                     quantity: int) -> tuple[str, str, int]:
        """Create an order for the warehouse.

        Args:
            warehouse (Warehouse): Warehouse to create order for
            item (str): Item to order
            quantity (int): Quantity of item to order

        Returns:
            tuple[str, str, int]: Status of order, item ordered, and quantity
        """
        if warehouse.in_stock(item):
            warehouse.take_from_stock(item, quantity)
            return ('ok', item, quantity)

        return ('not available', item, quantity)

    @staticmethod
    def create_order_fixed(warehouse: 'Warehouse',
                           item: str,
                           quantity: int) -> tuple[str, str, int]:
        """Create an order for the warehouse.

        Args:
            warehouse (Warehouse): _description_
            item (str): _description_
            quantity (int): _description_

        Returns:
            tuple[str, str, int]: _description_
        """
        if warehouse.in_stock_fixed(item, quantity):
            warehouse.take_from_stock(item, quantity)
            return ('ok', item, quantity)

        return ('not available', item, quantity)
