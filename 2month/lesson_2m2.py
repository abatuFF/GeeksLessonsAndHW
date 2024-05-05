class Animal:
    def __init__(self, name, age):
        self.__name = name
        if type(age) = int and age > 0:
            self.__age = age
        self.__was_born()

    def __was_born(self):
        print(f'Animal {self.__name} was born')

    def get_name(self):
        return self.__name

    def set_name(self, new_name):
        return self.__name = new_name

    def get_age(self, new_age):
        if type(new_age) == int and new_age >= 0:
            self.__age = new_age
        else:
            raise


    def info(self):
        return (f'{self.__name} is {self.__age} years. Birth year is {self.__age}')


# some_animal = Animal(name='Anim', age=2)
# some_animal.age = -3
# print(some_animal.info())


class Cat(Animal)