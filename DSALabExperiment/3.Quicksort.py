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

def quicksort(arr, low, high):
    if low < high:
        pivot = partition(arr, low, high)
        quicksort(arr, low, pivot-1)
        quicksort(arr, pivot+1, high)
    return arr

arr = [random.randint(0, 100) for _ in range(10)]
print("Original array:", arr)
quicksort(arr, 0, len(arr) - 1)
print("Sorted array:", arr)
