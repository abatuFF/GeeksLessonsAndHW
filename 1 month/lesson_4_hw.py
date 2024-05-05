max_days_in_month = {
    1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
    7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
}

while True:
    try:
        answer = input("Хотите продолжить? (да/нет): ")
        if answer.lower() == "нет":
            break
        elif answer.lower() != "да":
            print("Введена непральная дата, введите да или нет.")
            continue

        day = int(input("Введите день рождения: "))
        month = int(input("Введите месяц рождения: "))

        if (day < 1 or day > max_days_in_month.get(month, 0)) or (month < 1 or month > 12):
            print("Неверный формат даты.")
        else:
            if (month == 3 and day >= 21) or (month == 4 and day <= 19):
                zodiac_sign = "Овен"
            elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
                zodiac_sign = "Телец"
            elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
                zodiac_sign = "Близнецы"
            elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
                zodiac_sign = "Рак"
            elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
                zodiac_sign = "Лев"
            elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
                zodiac_sign = "Дева"
            elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
                zodiac_sign = "Весы"
            elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
                zodiac_sign = "Скорпион"
            elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
                zodiac_sign = "Стрелец"
            elif (month == 12 and day >= 22) or (month == 1 and day <= 19):
                zodiac_sign = "Козерог"
            elif (month == 1 and day >= 20) or (month == 2 and day <= 18):
                zodiac_sign = "Водолей"
            else:
                zodiac_sign = "Рыбы"

            print(f"Ваш знак зодиака: {zodiac_sign}")
    except ValueError:
        print("Ошибка: введите числовое значение.")
