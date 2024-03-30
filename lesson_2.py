# # bool
# word = "Geeks"
#
# print(word.istitle())
# print(word.isupper())
#
# # Сравнения
# print(5 == 7)
# print(5 != 7)
# print(5 > 7)
# print(5 < 7)
#
# # логические операторы
# # or,not,and
# print(not True and False)
# print(5 >= 7 and 81 < 2)

# условные операторы

#signal = input("Enter a color: ").lower()

#if signal == "red":
   # print("stop")
#elif signal == "green":
  #  print("go"),
#elif signal == "yellow":
 #   print("wait")
#else:
   # print("depends on situation")


#
# monday = (float(input("Enter your mondays expenses: ")))
#
# # переменная которой будет хранится суммированя выручка за все дни недели
# total_exp = monday
#
#
# # вывод недельной выручки
# if total_exp >= 1001:
#     print("you spend too much expenses")
# elif total_exp >= 300 and total_exp <= 1000:
#     print("you spend middle expenses")
# elif total_exp <= 0.5 and 299:
#     print("you spend too low expenses")
# else:
#     print("you spend nothing")


# print(f" Your total expenses for week is : {total_exp}")
# # вывод среденго дохода в день
# print(f" Your average expenses for day is : {average_exp}")

# задание с градусами

temperature = int(input("outside temperature: "))

if -30 <= temperature <= 10:
    print("there's cold outside")
elif 11 <= temperature <= 20:
    print("there's cool outside")
elif 21 <= temperature <= 30:
    print("there's heat outside")
else:
    print("you're form Mars?")
