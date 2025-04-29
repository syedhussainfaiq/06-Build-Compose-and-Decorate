class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, value):
        return value * self.factor

# Create an instance of the class with a specific factor
multiplier = Multiplier(3)

# Test callable() to check if the object is callable
print("Is 'multiplier' callable?", callable(multiplier))

# Call the object like a function
result = multiplier(5)
print("Result of calling 'multiplier(5)':", result)
