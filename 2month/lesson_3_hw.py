class Computer:
    def __init__(self, cpu, memory):
        self.__cpu = cpu
        self.__memory = int(memory)

    @property
    def cpu(self):
        return self.__cpu

    @cpu.setter
    def cpu(self, cpu):
        self.__cpu = cpu

    @property
    def memory(self):
        return self.__memory

    @memory.setter
    def memory(self, memory):
        self.__memory = memory

    def make_computations(self):
        return len(self.__cpu) * self.__memory

    def __str__(self):
        return f'Computer: CPU={self.__cpu}, Memory={self.__memory}'

class Phone:
    def __init__(self):
        self.__sim_cards_list = []

    @property
    def sim_cards_list(self):
        return self.__sim_cards_list

    @sim_cards_list.setter
    def sim_cards_list(self, sim_cards_list):
        self.__sim_cards_list = sim_cards_list

    def call(self, sim_card_number, call_to_number):
        if sim_card_number <= len(self.__sim_cards_list):
            sim_card = self.__sim_cards_list[sim_card_number - 1]
            print(f"Идет звонок на номер {call_to_number} с сим-карты {sim_card}")
        else:
            print("Ошибка: указан несуществующий номер сим-карты")

    def __str__(self):
        return f"Phone: SIM Cards={self.__sim_cards_list}"

class SmartPhone(Computer, Phone):
    def __init__(self, cpu, memory):
        super().__init__(cpu, memory)
        self.__sim_cards_list = ['+996 777 99 88 11']

    @property
    def sim_cards_list(self):
        return self.__sim_cards_list

    @sim_cards_list.setter
    def sim_cards_list(self, sim_cards_list):
        self.__sim_cards_list = sim_cards_list

    def use_gps(self, location):
        print(f"Using GPS to navigate to {location}")

    def __str__(self):
        return f"SmartPhone: CPU={self.cpu}, Memory={self.memory}, SIM Cards={self.sim_cards_list}"

    def __lt__(self, other):
        return self.memory < other.memory

    def __le__(self, other):
        return self.memory <= other.memory

    def __gt__(self, other):
        return self.memory > other.memory

    def __ge__(self, other):
        return self.memory >= other.memory

    def __eq__(self, other):
        return self.memory == other.memory

    def __ne__(self, other):
        return self.memory != other.memory

computer = Computer(cpu="Intel Core i7", memory=16)
phone = Phone()
smartphone1 = SmartPhone(cpu="Samsung CPU", memory=8)
smartphone2 = SmartPhone(cpu="Apple CPU", memory=12)

print(computer)
print(phone)
print(smartphone1)
print(smartphone2)

print("Результат вычислений на компьютере:", computer.make_computations())
phone.sim_cards_list = ["Beeline", "Megacom"]
phone.call(sim_card_number=1, call_to_number="+996 777 99 88 11")
smartphone1.use_gps(location="New York")

print("Является ли smartphone1 равным smartphone2?", smartphone1 == smartphone2)
print("Является ли smartphone1 не равным smartphone2?", smartphone1 != smartphone2)
print("Является ли smartphone1 больше smartphone2?", smartphone1 > smartphone2)
print("Является ли smartphone1 меньше или равным smartphone2?", smartphone1 <= smartphone2)
