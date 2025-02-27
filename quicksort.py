import random
import time

def quick_sort(array, low, high):
    stack = [(low, high)]
    while stack:
        low, high = stack.pop()
        if low < high:
            pivot_index = partition(array, low, high)
            if low < pivot_index - 1:
                stack.append((low, pivot_index - 1))
            if pivot_index + 1 < high:
                stack.append((pivot_index + 1, high))

def partition(array, low, high):
    pivot = array[high]
    index = low - 1
    for j in range(low, high, 1):
        if array[j] <= pivot:
            index += 1
            array[index], array[j] = array[j], array[index]
    array[index + 1], array[high] = array[high], array[index + 1]
    return index + 1

array = []
max_sort_numbers = int(input("Enter max numbers to sort: "))
for i in range(max_sort_numbers):
    array.append(random.randint(1, max_sort_numbers))
# print("unsorted array ",array, end='\n')
start_time = []

start_time.append(time.process_time())
quick_sort(array, 0, 100 - 1)
start_time.append(time.process_time())
quick_sort(array, 0, 1000 - 1)
start_time.append(time.process_time())
quick_sort(array, 0, 10000 - 1)
start_time.append(time.process_time())
quick_sort(array, 0, 100000 - 1)
start_time.append(time.process_time())
quick_sort(array, 0, 1000000 - 1)
start_time.append(time.process_time())
quick_sort(array, 0, 10000000 - 1)
start_time.append(time.process_time())
print("Sorting times for 100: ", start_time[1] - start_time[0])
print("Sorting times for 1000: ", start_time[2] - start_time[1])
print("Sorting times for 10000: ", start_time[3] - start_time[2])
print("Sorting times for 1000000: ", start_time[4] - start_time[3])
print("Sorting times for 10000000: ", start_time[5] - start_time[4])


# print("Sorted array :", array, end='\n')
