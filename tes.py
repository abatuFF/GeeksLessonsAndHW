week_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'friday', 'Saturday', 'sunday']
amount_days = len(week_days)
expenses = 0

for day in week_days:
    print(f'you total expenses is {expenses}')
    expense = int(input(f'enter your expenses in {day.upper()}'))
    print(day.upper(), expense)
    expenses += expense

