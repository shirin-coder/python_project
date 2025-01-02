class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

class Shop:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)
        print(f"Product {product.name} added successfully!")

    def buy_product(self, product_name, quantity):
        for product in self.products:
            if product.name == product_name:
                if product.quantity >= quantity:
                    product.quantity -= quantity
                    print(f"Successfully bought {quantity} {product_name}(s).")
                    print("Congress: Purchase successful!")
                    return
                else:
                    print(f"Sorry, not enough stock for {product_name}.")
                    return
        print(f"Product {product_name} not found in the shop.")

# Example usage:
# Creating shop and products
shop = Shop()
p1 = Product("Laptop", 1000, 5)
p2 = Product("Phone", 500, 10)

# Adding products to the shop
shop.add_product(p1)
shop.add_product(p2)

# Buying a product
shop.buy_product("Laptop", 2)
shop.buy_product("Phone", 12)  # Not enough stock example
shop.buy_product("Tablet", 1)  # Product not found example
shop.buy_product("laptop",8)
shop.buy_product("Phone",8)