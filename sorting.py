# Sorting Algorithms

# Bubble Sort Algorithm Implementation

numbers = [3,1,2,5]


def bubble_sort(data):
    length = len(data)
    if length <= 1:
        return data
    for i in data:
        for j in range(0, length - 1):
            if data[j] < data[j + 1]:
                temp = data[j]
                data[j] = data[j + 1]
                data[j + 1] = temp


# bubble_sort(numbers)
# print(numbers)

# Selection Sort Algorithm

def selection_sort(data):
    for i in range(0, len(data)):
        smallest_number = i
        temp = data[i]
        for j in range(i + 1, len(data)):
            if data[j] < data[smallest_number]:
                smallest_number = j
        data[i], data[smallest_number] = data[smallest_number], temp


# selection_sort(numbers)
# print(numbers)


# Insertion Sort Algorithm:

def insertion_sort(data):
    for i in range(1, len(data)):
        key_item = data[i]
        j = i - 1
        while j >= 0 and data[j] > key_item:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = key_item


# insertion_sort(numbers)
# print(numbers)

# Merge Sort Algorithm

# def merge(left, right):
#     print(left, right)
#     result = []
#     left_index = 0
#     right_index = 0
#     while left_index < len(left) and right_index < len(right):
#         if left[left_index] < right[right_index]:
#             result.append(left[left_index])
#             left_index += 1
#         else:
#             result.append(right[right_index])
#             right_index += 1
#     result.extend(left[left_index:])
#     result.extend(right[right_index:])
#     print(result)
#     return result
#
#
# def merge_sort(data):
#     if len(data) == 1:
#         return data
#     m = len(data) // 2
#     l = data[:m]
#     r = data[m:]
#     return merge(merge_sort(l), merge_sort(r))


# merge_sort([9, 7, 10, 3, 5])


def merge(left, right):
    result = []
    left_index = 0
    right_index = 0
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1
    result.extend(left[left_index:])
    result.extend(right[right_index:])
    print(result)
    return result


def merge_sort(data):
    if len(data) == 1:
        return data
    m = len(data) // 2
    l = data[:m]
    r = data[m:]
    return merge(merge_sort(l), merge_sort(r))


# merge_sort([9, 7, 8, 10])


# Quick Sort

def partition(l, r, data):
    ptr, pivot = l, data[r]
    for i in range(l, r):
        if data[i] <= pivot:
            data[i], data[ptr] = data[ptr], data[i]
            ptr += 1
    data[r], data[ptr] = data[ptr], data[r]
    return ptr


def quick_sort(l, r, data):
    if l < r:
        pi = partition(l, r, data)
        quick_sort(l, pi - 1, data)
        quick_sort(pi + 1, r, data)
    return data


print(quick_sort(0, len(numbers) - 1, numbers))
