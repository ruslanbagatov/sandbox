class Car:
    count_of_cars = 0
    count_of_liters = 0
    is_engine_works = False

    def __init__(self, model, fuel_tank_size):
        self.model = model
        self.fuel_tank_size = fuel_tank_size
        Car.count_of_cars += 1
        print(f'Car {self.model} created. Fuel tank is empty')

    def add_fuel(self, liters):
        self.count_of_liters += liters
        print(f'You added {liters} liters')

    def start_engine(self):
        if self.count_of_liters == 0:
            print('Fuel tank is empty. Add the fuel!')
        else:
            print('Engine started!')
            self.is_engine_works = True

    def shutdown_engine(self):
        print(f'Engine off!. You have {self.count_of_liters} liters of petrol.')
        self.is_engine_works = False

    def is_engine_working(self):
        if self.is_engine_works:
            print('Engine works.')
            self.count_of_liters -= 1
        else:
            print('Engine stay turned off.')


car_1 = Car('Mercedes', 20)
