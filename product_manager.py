from product import Product

class ProductManager:
    def __init__(self):
        self.products = []  # lista cu toate produsele disponibile

    def add_product(self, product: Product):
        self.products.append(product)

    def display_products(self):
        if not self.products:
            print("Nu exista produse disponibile.")
            return
        for product in self.products:
            product.display_info()

    def total_inventory_value(self):
        total = 0
        for product in self.products:
            total += product.price * product.quantity
        return total