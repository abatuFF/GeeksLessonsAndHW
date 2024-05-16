def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


unsorted_list = [9,6,8,7,1,4,5,2,3]
sorted_list = bubble_sort(unsorted_list)
print(f'Sorted list: {sorted_list}')