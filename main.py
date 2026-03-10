from product import Product
from product_manager import ProductManager

def main():
    manager = ProductManager()

    p1 = Product("Laptop", 3500.0, 5)
    p2 = Product("Mouse", 80.0, 20)
    p3 = Product("Tastatura", 150.0, 10)

    manager.add_product(p1)
    manager.add_product(p2)
    manager.add_product(p3)

   # am eliminat afisarea inventarului si valoarea totala

if __name__ == "__main__":
    main()