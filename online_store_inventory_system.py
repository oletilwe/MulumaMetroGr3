# created a class called product. 
class Product:
    #initialize the class
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def sell(self, quantity): # sell function
        # it checks if the users stated quantity is more then the stock in hand. 
        if quantity > self.stock:
            # if thats the case it raises an error stating that the stock isnt enough
            raise ValueError("Not enough stock to fulfill the order")
        self.stock -= quantity
        # here if the stock is enough the customers quantity is minused from the stock 
        return self.price * quantity
    # this returns the price of the one product multiply by the quantity of the products. 


# class called electronics that inherites the product class
class Electronics(Product):
    def __init__(self, name, price, stock, warranty_years):
        super().__init__(name, price, stock)
        self.warranty_years = warranty_years

# this also inherits the product class
class Book(Product):
    def __init__(self, name, price, stock, author):
        super().__init__(name, price, stock)
        self.author = author

# new class with no inheritens called inventory
class Inventory:
    def __init__(self):
        self.catalog = []
# this function(method) adds a new product to the products already available using the .append function. 
    def add_product(self, product):
        self.catalog.append(product)

    def find_product_by_name(self, name):
        # a for loop that looks for the specific product in the catalog. 
        for product in self.catalog:
            if product.name.lower() == name.lower():
                # if the product that is in lowercase is there, it returns the product. 
                return product
            # else it returns nothing cause the product isnt there. 
        return None

    def restock(self, name, amount):
        product = self.find_product_by_name(name)
        if product:
            product.stock += amount
            print(f"Product {name} restocked successfully.")
        else:
            print(f"Product {name} not found in the catalog.")

    def search(self, name=None):
        results = []
        for product in self.catalog:
            if name and product.name.lower().startswith(name.lower()):
                results.append(product)
        return results


def process_order(inventory, order_list):
    total = 0
    for product_name, quantity in order_list:
        product = inventory.find_product_by_name(product_name)
        if product:
            try:
                revenue = product.sell(quantity)
                total += revenue
                print(f"Sold {quantity} units of {product_name}. Remaining stock: {product.stock}")
            except ValueError as e:
                print(f"Error processing order for {product_name}: {e}")
        else:
            print(f"Product {product_name} not found in the catalog.")
    return total


def main():
    inventory = Inventory()

    apple = Product("Apple", 1.00, 100)
    smartphone = Electronics("Smartphone", 500.00, 20, 2)
    book = Book("Python Programming", 50.00, 50, "John Doe")

    inventory.add_product(apple)
    inventory.add_product(smartphone)
    inventory.add_product(book)

    orders = [
        [("Apple", 10), ("Smartphone", 2), ("Python Programming", 5)],
        [("Apple", 20), ("Smartphone", 1), ("Unknown Product", 1)]
    ]

    for i, order in enumerate(orders):
        print(f"Processing Order {i+1}:")
        total = process_order(inventory, order)
        print(f"Order Total: ${total:.2f}\n")

    inventory.restock("Apple", 50)
    print(f"Apple stock after restocking: {inventory.find_product_by_name('Apple').stock}")

    print("Searching for products:")
    results = inventory.search(name="S")
    for product in results:
        print(product.name)


if __name__ == "__main__":
    main()