def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i -1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        return arr

unsorted_list = [1, 3, 5, 4, 7, 6, 8, 9, 10]
sorted_list = bubble_sort(unsorted_list)

print(f'Sorted list : {sorted_list}')


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        return arr

unsroted_list = [1, 3, 5, 4, 7, 6, 8, 9, 10]
sorted_list = bubble_sort(unsroted_list)
print(f' Sorted List: {sorted_list}')



def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] == arr[j + 1], arr[j]
        return arr

unsorted_list = [1, 3, 5, 4, 7, 6, 8, 9, 10]
sorted_list = bubble_sort(unsorted_list)
print(f'sorted list : {sorted_list}')