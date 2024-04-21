#функция ближайшее число
def nearest_number(numbers, target):
    sorted_numbers = sorted(numbers, key=lambda x: abs(x - target))
    return target, sorted_numbers



# Пример с filter
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filtered_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(filtered_numbers)  # Вывод: [2, 4, 6, 8, 10]

# Пример с map
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x ** 2, numbers))
print(squared_numbers)  # Вывод: [1, 4, 9, 16, 25]
