# Base class Vehicle
class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    
    def display_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Year: {self.year}")


# Car class inheriting from Vehicle
class Car(Vehicle):
    def __init__(self, brand, model, year, num_doors):
        super().__init__(brand, model, year)
        self.num_doors = num_doors
    
    def display_info(self):
        super().display_info()
        print(f"Number of doors: {self.num_doors}")


# Bike class inheriting from Vehicle
class Bike(Vehicle):
    def __init__(self, brand, model, year, bike_type):
        super().__init__(brand, model, year)
        self.bike_type = bike_type
    
    def display_info(self):
        super().display_info()
        print(f"Type: {self.bike_type}")


# Create objects and call display_info()
if __name__ == "__main__":
    # Create a Car object
    car = Car("Toyota", "Camry", 2023, 4)
    print("Car information:")
    car.display_info()
    print()
    
    # Create a Bike object
    bike = Bike("Trek", "FX 3", 2022, "road")
    print("Bike. information:")
    bike.display_info()
