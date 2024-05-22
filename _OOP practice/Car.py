class Car:
    def __init__(self, make, model, year, odometer_reading = 0):
        self.__make = make
        self.__model = model
        self.__year = year
        self.__odometer_reading = odometer_reading

    def get_descriptive_name(self):
        print(self.__make, self.__model, self.__year)

    def read_odometer(self):
        print(f' cars odometer is : {self.__odometer_reading}')

    def update_odometer(self, new_odometer):
        if new_odometer >= self.__odometer_reading:
            self.__odometer_reading = new_odometer
        else:
            print('You can\'t roll back!')

    def increment_odometer(self, miles):
        if miles >= 0:
            self.__odometer_reading += miles
        else:
            print("Increment must be positive")




BmwCar = Car('BMW', 'X5', 2020)
print(BmwCar.get_descriptive_name())
BmwCar.read_odometer()

BmwCar.update_odometer(1500)
BmwCar.read_odometer()

BmwCar.increment_odometer(500)
BmwCar.read_odometer()

BmwCar.update_odometer(1400)
BmwCar.read_odometer()

BmwCar.increment_odometer(200)
BmwCar.read_odometer()