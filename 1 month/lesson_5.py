#схема функции
# определение  наименование(параметры):
#     тело функции
#     возврат результата
#
# вызов функции
# наименование(аргументы)


# def get_data(name, surname = 'unknown'):
#     return f'name: {name} surname: {surname}'
#
# print(get_data('danya', 'siletov'))
#



# lenght = 6
# width = 5
# square_3 = lenght * width
# print(square_3)
#
# lenght = 320
# width = 140
# square_victory = lenght * width
# print(square_victory)
#

# def get_square(lenght, width):
#     square = lenght * width
#     return square
#
#
# square_3 = get_square(6,5)
# square_victory = get_square(320, 140)
#
# print(square_3)
# print(square_victory)


def get_answer_temperature(temperature):
    if -30 <= temperature <= 10:
        return 'cold'
    elif 11 <= temperature <= 20:
        return 'cool'
    elif 21 <= temperature <= 30:
        return 'warm'
    elif 30 <= temperature <= 40:
        return 'hot'
    else:
        return 'dangerous'

while True:
    temperature = input("enter temp or 'stop' ")
    if temperature == 'stop':
        print("exit")
        break
    elif temperature.isnumeric():
        answer = get_answer_temperature(int(temperature))
        if answer == 'cold':
            print(f'take care there {temperature} outside')
        elif answer == 'cool':
            print(f'take a jacket there {temperature} outside')
        elif answer == 'warm':
            print(f'take easy clothe theres {temperature} outside')
        elif answer == 'hot':
            print(f'go swim in lake')
        else:
            print(f' GET BACK, THERES {temperature} OUTSIDE!!!')
    else:
        print('type only numbers')