class Car:
    # Public variable
    brand = "Toyota"

    # Public method
    def start (self) :
        return f"The {self.brand} car is starting!"
    

# Instantiate the Car class
my_car = Car()


# Access the public variable
print("Car brand",my_car.brand)


# Access the public method
print(my_car.start())