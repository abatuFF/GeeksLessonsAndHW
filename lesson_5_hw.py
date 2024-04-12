def calculate_discount(homework_points, test_points, attendance):
    discount = 0

    if homework_points >= 80 and test_points >= 80 and attendance >= 8:
        discount = 3000
    elif homework_points >= 70 and test_points == 60 and attendance >= 8:
        discount = 2500
    elif  homework_points >= 70 and test_points >= 60 and attendance >= 7:
        discount = 2000
    elif homework_points >= 60 and test_points >= 80 and attendance >= 7:
        discount = 2000
    elif homework_points >= 60 and test_points >= 60 and attendance >= 6:
        discount = 2000
    elif homework_points >= 50 and  test_points >= 60 and attendance >= 6:
        discount = 1000
    return discount


while True:
    agreement = input("Введите 'да' чтобы продолжить, и 'нет' чтобы выйти: ")
    if agreement.lower() == 'нет':
        print("закрытие кода")
        break
    elif agreement.lower() == 'да':
        payment_amount = 14000
        homework_points = int(input("Введите баллы за домашнее задание: "))
        test_points = int(input("Введите баллы за тесты: "))
        attendance = int(input("Введите количество посещений: "))


        discount_amount = calculate_discount(homework_points, test_points, attendance)
        total_price = discount_amount - payment_amount


        if discount_amount > 0:
            print(f"Вы получаете скидку в размере {discount_amount} рублей. К оплате у вас {total_price} сом")
        else:
            print("К сожалению, вы не получаете скидки.")
    else:
        print("Пожалуйста введите только 'да' или 'нет' ")
