#словари

new = dict(enumerate('python'))
new1 = dict([[0, 'g'], [2, 'o']])
new3 = dict(name='jessica', age=18, country='India')

students = {
    'name': 'azamat',
    'age': 19,
    'height': 1.78,
    'is_married': False,
    'languages': ['english', 'russian'],
    'education': ('school', 'college'),
}
#
# #
# # print(students)
# # print(students['name'])
# # print(students.get('languages', 'theres no key'))
# # print(new)
# # print(new1)
# # print(new3)
#
#
# # add
# students['surname'] = 'isakov'
# students.update(new3)
# #edit
# #заменить объект в словаре
# students['age'] = 20
# #заменить объект в списке
# students['languages'][0] = 'kyrgyz'
# #превратить объект в словаре в список
# students['education'] = list(students['education'])
# students['education'].append('python')
# students['education'] = tuple(students['education'])
#
# #delete
# deleted = students.pop('is_married')
# del students['height']

# вывод словаря с столбике
# for key, value in students.items():
#     print(f'{key}: {value}')

# for i in students:
#     print(f'{i} : {students[i]}')
#
# days = ('mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun')
#
# expenses = {}
#
# for day in days:
#     expense = int(input(f'Enter a expense in a {day}'))
#     expenses[day] = expense
#
# for day , expense in expenses.items():
#     print(f'{day.upper()} : {expense}')
#
# total_expenses = sum(expenses.values())
# print(
#     f'total expenses: {total_expenses}\n'
#     f'average expense: {"%.2f" % (total_expenses / len(days))}'
# )
#
# numbers = [1, 2, 3, 4, 5, 3, 6, 1]
# numbers1 = {1, 2, 3, 4, 5, 3, 6, 1}
#
# print(numbers)
# print(numbers1)
# print(type(numbers1))

beshbarmak = {'et', 'kakmyr', 'piyaz'}
plov = {'rice', 'et', 'carrot'}

print(beshbarmak.union(plov))
print(beshbarmak | plov)

print(beshbarmak.difference(plov))
print(beshbarmak - plov)

print(beshbarmak.intersection(plov))
print(beshbarmak & plov)

print(beshbarmak.symmetric_difference(plov))
print(beshbarmak ^ plov)
