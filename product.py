# impliment methods for creating, updating, and suspending products
class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.is_active = True

    def create_product(self):
        return f"Product '{self.name}' created."

    def update_product(self, name=None, price=None):
        if name:
            self.name = name
        if price:
            self.price = price
        return f"Product '{self.product_id}' updated."

    def suspend_product(self):
        self.is_active = False
        return f"Product '{self.name}' suspended."