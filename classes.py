class Vehicle:
    count = 0
    def __init__(self, type):
        self.type = type

    def start_engine(self):
        print('Engine started!')

    def shutdown_engine(self):
        print('Engine off!')



class Car(Vehicle):

    fuel_count = 0

    def __init__(self, fuel_type):
        self.fuel_type = fuel_type

    def add_fuel(self, liters):
        self.fuel_count += liters


mazda = Car('petrol')
print(mazda.fuel_count)
