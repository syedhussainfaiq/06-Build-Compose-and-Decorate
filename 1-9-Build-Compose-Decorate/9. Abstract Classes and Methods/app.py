from abc import ABC, abstractmethod

# Abstract base class
class Shape(ABC):
    @abstractmethod
    def area(self):
        """Abstract method to calculate area."""
        pass


# Subclass implementing the abstract method
class Reactangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area (self):
        """Implementation of the abstract method"""
        return self.width * self.height

 # Examlpe usage
if __name__ == "__main__":
    try:
        shape =Shape() # This will raise an errror as Shape abstractexcept TypeError as e:
    except TypeError as e:
      print(f"Cannot instantiate abstract class: {e}")

    rect = Reactangle(5, 10)
    print(f"Area of rectangle: {rect.area()}") # Output: Area of reactangle 50

        