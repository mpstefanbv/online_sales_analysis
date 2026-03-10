from product import Product
from product_manager import ProductManager
from cart import Cart
import random

def main():
    manager = ProductManager()

    p1 = Product("Laptop", 3500.0, 5)
    p2 = Product("Mouse", 80.0, 20)
    p3 = Product("Tastatura", 150.0, 10)
    p4 = Product("Monitor", 900.0, 7)

    manager.add_product(p1)
    manager.add_product(p2)
    manager.add_product(p3)
    manager.add_product(p4)

    print("Produse disponibile:")
    manager.display_products()
    print(f"Valoarea totala a inventarului: {manager.total_inventory_value()}")
    
    cart = Cart()
    
    available_products = manager.products
    selected_products = random.sample(available_products, 3)

    for prod in selected_products:
        cart.add_to_cart(prod)

    cart.display_cart()
    print(f"Valoarea totala de plata a cosului: {cart.total_cart_value()}")

if __name__ == "__main__":
    main()