# Given two inputs, in this case, two arrays, merge them sorted

# My solution
def merge_sorted(array1, array2):

    if type(array1) is not list or type(array2) is not list:
        return

    if len(array1) < 1:
        return array2

    if len(array2) < 1:
        return array1

    array1.sort()
    array2.sort()

    merged_array = []
    i = 0
    j = 0

    while i < len(array1) or j < len(array2):
        if array1[i] >= array2[j]:
            merged_array.append(array2[j])
            j += 1
        else:
            merged_array.append(array1[i])
            i += 1

        if i == len(array1):
            merged_array += array2[j:]
            break

        if j == len(array2):
            merged_array += array1[i:]
            break

    print(merged_array)
    return merged_array

merge_sorted([2, 4, 6], [1, 3, 4, 5])
