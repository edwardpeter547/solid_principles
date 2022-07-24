from dataclasses import dataclass, field
from functools import reduce
from typing import List
from enum import Enum

@dataclass
class Item:
    __name: str
    __quantity: int = 0
    __price: float = 0.00
    
    
    @property
    def name(self):
        return self.__name
    
    
    @name.setter
    def name(self, value):
        self.__name = value
        
    
    @property
    def quantity(self):
        return self.__quantity
    
    
    @quantity.setter
    def quantity(self, value):
        self.__quantity = value
        
    
    @property
    def price(self):
        return self.__price
    
    
    @price.setter
    def price(self, value):
        self.__price = value
    

class OrderStatus(Enum):
    open = "open"
    paid = "paid"

      
class Order:
    line_items: List[Item] = []
    status: OrderStatus = OrderStatus.open
    
    
    def add_item(self, item: Item):
        self.line_items.append(item)
        
    def total_price(self):
        total = 0.00
        for item in self.line_items:
            total += item.quantity * item.price
        return total
    
    