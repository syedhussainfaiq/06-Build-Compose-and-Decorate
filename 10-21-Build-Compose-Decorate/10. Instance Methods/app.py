class Dog:
    def __init__(self, name, breed):
        # Initialize instance variables
        self.name = name
        self.breed = breed

    def bark(self):
        # Instance method that uses instance variables
        print(f"{self.name} the {self.breed} says: Woof! Woof!")

# Example usage
dog1 = Dog("Buddy", "Golden Retriever")
dog2 = Dog("Max", "Bulldog")

# Call the bark method
dog1.bark()
dog2.bark()
