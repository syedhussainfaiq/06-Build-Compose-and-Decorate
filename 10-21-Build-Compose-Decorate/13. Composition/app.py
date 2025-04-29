class Engine:
    def __init__(self, horsepower, fuel_type):
        self.horsepower = horsepower
        self.fuel_type = fuel_type

    def start(self):
        return f"The {self.horsepower} HP {self.fuel_type} engine is starting."

class Car:
    def __init__(self, make, model, engine: Engine):
        self.make = make
        self.model = model
        self.engine = engine

    def start_car(self):
        return f"{self.make} {self.model} is starting. {self.engine.start()}"

# Example usage
engine = Engine(horsepower=150, fuel_type="petrol")
car = Car(make="Toyota", model="Corolla", engine=engine)

print(car.start_car())
