class Transport:
    def __init__(self, the_model, the_year, the_color):
        self.model = the_model
        self.year = the_year
        self.color = the_color

class Plane:
    def __init__(self, the_model, the_year, the_color, penalties=0, load_capacity=0):
        super().__init__(the_model, the_year,the_color, penalties)
        self.load_capacity = load_capacity

    def load_cargo(self, weight, type_of):
        if weight > self.load_capacity:
            print(f'You cannot load more than {self.load_capacity} kg.')
        else:
            print(f'Cargo of {type_of} was successfully loaded into {self.model}.')
class Car:
    counter = 0    # constructor
    def __init__(self, the_model, the_year, the_color, penalties=0):
        # attributes\fields
        self.model = the_model
        self.year = the_year
        self.color = the_color
        self.penalties = penalties
        Car.counter += 1
    def drive(self, city, speed):
        print(f' Car {self.model} is driving to {city} with speed {speed}')

    def change_color(self, new_color):
        self.color = new_color

bmw_car = Car('BMW X7', 2020, 'red')
print(f'MODEl: {bmw_car.model} YEAR: {bmw_car.year} COLOR: {bmw_car.color}')

honda_car = Car(the_color = "Yellow", the_model = "Honda Fit", the_year = 2020, penalties =500)
print(f'MODEL: {honda_car.model} YEAR: {honda_car.year} COLOR: {honda_car.color}')
#
bmw_car.drive('Osh', 100)
bmw_car.drive('batken',  90)
honda_car.drive('Kant', 70)


volvo_truck = Truck('Volvo 400', 2019, 'blue', 1200, 45000)

print(f'MODEL: {volvo_truck.model} YEAR: {volvo_truck.year} COLOR: {volvo_truck.color}')