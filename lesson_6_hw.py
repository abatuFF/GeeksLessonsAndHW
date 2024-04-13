data_tuple = ('h', 6.13, 'C', 'e', 'T', True, 'k', 'e', 3, 'e', 1, 'g')


letters = [item for item in data_tuple if isinstance(item, str)]
numbers = [item for item in data_tuple if isinstance(item, int)]


letters.append(True)
numbers.remove(1)
numbers.insert(1, 2)

numbers.sort()
letters.reverse()

numbers = [num**2 for num in numbers]

letters[1] = 'G'
letters[-2] = 'c'

print(tuple(letters))
print(tuple(numbers))