# переменные в которых будут хранится доходы за каждый из дней
monday = (float(input("Enter your mondays expenses: ")))
tuesday = (float(input("Enter your tuesday expenses: ")))
wednesday = (float(input("Enter your wednesday expenses: ")))
thursday = (float(input("Enter your thursday expenses: ")))
friday = (float(input("Enter your friday expenses: ")))
saturday = (float(input("Enter your saturday expenses: ")))
sunday = (float(input("Enter your sunday expenses: ")))

# переменная которой будет хранится суммированя выручка за все дни недели
total_exp = monday + tuesday + wednesday + thursday + friday + saturday + sunday

# переменная в которой будет вычеслятся средний доход в день
average_exp = round(total_exp / 7, 1)


# вывод недельной выручки
print(f" Your total expenses for week is : {total_exp}")
# вывод среденго дохода в день
print(f" Your average expenses for day is : {average_exp}")