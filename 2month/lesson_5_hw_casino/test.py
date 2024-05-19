class Car:
    def __init__(self, make, model, year, odometer_reading = 0):
        self.__make = make
        self.__model = model
        self.__year = year
        self.__odometer_reading = odometer_reading

    def get_descriptive_name(self):
        return f'{self.__year}, {self.__make}, {self._model}'


    