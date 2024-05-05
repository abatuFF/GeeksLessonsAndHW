# students2 = ['cholpon', 'aliya']
# students = ['azhibek', 'omurbek', 'kanatbek', 'daniel', 'omurbek']


#index
# print(sudents)
# print(sudents[1])
# print(sudents[-1])
# print(type(sudents))

#slice
# print(sudents[1:3])
# print(sudents[:3])
# print(sudents[::2])

# list function
# new = list('geeks')
# numbers = list(range(1,6))
#
# print(numbers)
# print(new)


# adding objects in list.
# students.append('kumushai')
# students.insert(2, 'aisen')
# # students.extend(students2)
# students += students2
# print(students)

#edit
#сортировка списка по алфавиту
# students.sort()
#сортировка против алфавита
# students.sort(reverse=True)

# отзеркаливание списка
# students.reverse()

# замена объекта
# students[1] = 'timur'

# замена двух объектов
# students[2:] = ['kumushai', 'cholpon']

#замена мест двух объектов
# students[0], students[2], = students[2], students[0]

#delete
# удаление по значению
# students.remove('kanatbek')
#
# удаление по индексу
# students.pop(-1)
# вырезание объекта

# deleted = students.pop(-1)
# print(list(deleted))
# print(students)

# вырезать несколько
# del students2[:2]


# узнать индекс объекта
# print(students.index('omurbek'))
# print(students.index('omurbek', 2))
# # узнать количество всех одинаковых объектов
# print(students.count('omurbek'))

# # копии списков
# new_list = students[::]
# print(id(students))
# print(id(new_list))
#
# # проверка являются ли занчения в списке одинковыми
# print(students == new_list)
# # проверка является ли индекс в списках одним и тем же
# print(students is new_list)
#
# # new_list[0] = 'timur'
#
# print(students)
# print(new_list)

# циклы со списками
# for students in students:
#     print(students.upper())


#добавить обработку ошибок
# первая домашка с листами
week_days = ['Monday', 'Tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
amount_days = len(week_days)
expenses = 0

for day in week_days:
    print(f'total sum: {expenses}')
    expense = int(input(f'Enter expenses in {day.upper()}: '))
    print(day.upper(), expense)
    expenses += expense

# numbers = [23, 14, 12, 2, 5]
# numbers.sort(reverse = True)
#
# print(min(numbers))
# print(max(numbers))
# print(sum(numbers))

#
# students = 'azhibek', 'omurbek', 'kanatbek', 'daniel', 'omurbek'
#
# students = list(students)
# students = tuple(students)
# print(students)
# print(type(students))

# list compreheshion
# объект цикл последовательность условие

students = 'azhibek', 'omurbek', 'kanatbek', 'daniel', 'omurbek'

students2 = [students.upper() for students in students if 'a' in students]

print(students)
print(students2)






