from product import Product

class Cart:
    def __init__(self):
        self.cart_items = []  # lista de produse din cos

    def add_to_cart(self, product: Product):
        self.cart_items.append(product)

    def total_cart_value(self):
        total = 0
        for product in self.cart_items:
            total += product.price * product.quantity
        return total

    def display_cart(self):
        if not self.cart_items:
            print("Cosul este gol.")
            return
        print("Continutul cosului:")
        for product in self.cart_items:
            product.display_info()