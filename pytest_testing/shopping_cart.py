from typing import List

class ShoppingCart():
    
    def __init__(self , max_size):
        self.items: List[str] = []
        self.max_size = max_size

    def add_item_to_cart(self, item ):
        if self.size() == self.max_size:
            raise OverflowError("cannot add more than 5 items")
        self.items.append(item)
    
    def size(self):
        return len(self.items)

    def get_items(self):
        return self.items

    def get_total_price_of_items_in_dict(self, price_map ):
        total = 0 
        for item,price in price_map.items():
            total += price
        return total
        
