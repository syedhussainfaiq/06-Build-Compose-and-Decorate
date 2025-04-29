class Product:
    def __init__(self, price):
        self._price = price  # Private attribute

    @property
    def price(self):
        """Getter method for price"""
        return self._price

    @price.setter
    def price(self, value):
        """Setter method for price"""
        if value < 0:
            raise ValueError("Price cannot be negative!")
        self._price = value

    @price.deleter
    def price(self):
        """Deleter method for price"""
        print("Deleting price...")
        del self._price

# Example usage
product = Product(100)

# Get the price
print("Initial Price:", product.price)

# Set the price
product.price = 150
print("Updated Price:", product.price)

# Attempt to set a negative price
try:
    product.price = -50
except ValueError as e:
    print("Error:", e)

# Delete the price
del product.price

# Verify deletion
try:
    print(product.price)
except AttributeError as e:
    print("Error:", e)
