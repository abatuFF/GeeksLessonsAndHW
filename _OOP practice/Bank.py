class BankAccount:
    def __init__(self, owner, balance):
        self.__owner = owner
        self.__balance = balance

    def deposit(self):
        if self.__balance <= 0:
            return f'You dont have any money, or have some credits'
        else:
            return f'You have {self.__balance}, on your deposit'

    def withdraw(self, amount):
        if amount > 0:

        