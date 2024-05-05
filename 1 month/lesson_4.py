# #обработка исключений
# try:
#     тут проводиться код
# except:
#     обрабатывается ошибка
# else:
#     в случае если ошибку не нашли
# finally:
#     завершение ошибки
#
# try:
#     print(2 * "s")
# except:
#     print("error detected")
# else:
#     print("error not finded")
# finally:
#     print("error ended")

# results = ''
#
# while True:
#     print(results)
#     try:
#         num1 = int(input('Enter a number one: '))
#         num2 = int(input('Enter a number two: '))
#         print(num1 / num2)
#         results += f'{num1} / {num2} = {num1 / num2}\t'
#     except ValueError:
#         print("enter only numbers")
#     except ZeroDivisionError:
#         print("you cant devide to zero")


while True:
    time = input("Enter the time of day (morning, day, evening, night), to exit enter (exit) or (stop): ").lower()

    if time == "morning":
        print("Good morning!")
    elif time == "day":
        print("Good day!")
    elif time == "evening":
        print("Good evening!")
    elif time == "night":
        print("Good night!")
    elif time == "stop" or time == "exit":
        print("Exiting the program.")
        break
    else:
        print("Please enter a valid time of day or 'stop'/'exit' to end.")
