import random

def partition(arr, low, high):
    pivot = random.randint(low, high)
    pivot_val = arr[pivot]
    arr[pivot], arr[high] = arr[high], arr[pivot]
    pivot_index = low
    for i in range(low, high):
        if arr[i] < pivot_val:
            arr[i], arr[pivot_index] = arr[pivot_index], arr[i]
            pivot_index += 1
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
    return pivot_index

def quickselect(arr, low, high, k):
    if low == high:
        return arr[low]
    pivot_index = partition(arr, low, high)
    if k == pivot_index:
        return arr[k]
    elif k < pivot_index:
        return quickselect(arr, low, pivot_index - 1, k)
    else:
        return quickselect(arr, pivot_index + 1, high, k)

def find_median(arr):
    n = len(arr)
    median = quickselect(arr, 0, n - 1, n // 2)
    if n % 2 == 0:
        median = (median + quickselect(arr, 0, n - 1, n // 2 - 1)) / 2
    return median

arr = [1,2,3,4,5,6,7,8,9]
print(find_median(arr))
