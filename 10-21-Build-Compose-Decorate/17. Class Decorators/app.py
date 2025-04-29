# Define the class decorator
def add_greeting(cls):
    def greet(self):
        return "Hello from Decorator!"
    cls.greet = greet
    return cls

# Apply the decorator to a class
@add_greeting
class Person:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        return f"My name is {self.name}."

# Create an instance of the decorated class
person = Person("Hussain")

# Call the greet method added by the decorator
print(person.greet())

# Call the original method to confirm functionality remains intact
print(person.introduce())
