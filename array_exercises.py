# Exercise 1
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

def return_sum_indices(integers, target):
    first_addend = 0
    second_addend = 0

    for i in integers:
        for j in integers[integers.index(i) + 1:]:
            if i + j == target:
                first_addend = integers.index(i)
                second_addend = integers[first_addend + 1:].index(j) + first_addend + 1
                print(first_addend, second_addend)
                return [first_addend, second_addend]


return_sum_indices([3,4,2,5,7], 6)

# Exercise 2
# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
# Note that you must do this in-place without making a copy of the array.


def move_zeroes(array):

    # Checking
    if len(array) <= 1 or 0 not in array:
        print(array)
        return array

    occurrences = array.count(0)
    current_index = array.index(0)
    last_index = len(array) - 1
    zeroes_moved = 0

    while current_index != last_index:
        current_element = array[current_index]
        next_element = array[current_index + 1]
        array[current_index], array[current_index + 1] = next_element, current_element
        current_index += 1

        if current_index == last_index:
            current_index = array.index(0)
            zeroes_moved += 1

        if zeroes_moved == occurrences:
            break

    print(array)
    return array


move_zeroes([1,0,2,0,3,4])

# Exercise 3
# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

# My Solution

def check_duplicates(array):
    for i in array:
        for j in array:
            if i == j:
                print(True)
                return True
    print(False)
    return False

# Other Solutions

def check_duplicates2(array):
    elements = {}
    for i in array:
        if elements.get(i):
            print(True)
            return True
        elements[i] = 1
    print(False)
    return False


def check_duplicates3(array):
    if set(array) == array:
        print(False)
        return False
    print(True)
    return True

check_duplicates([1, 6, 3, 5, 7, 3, 2, 1])
check_duplicates2([1, 6, 3, 5, 7, 3, 2, 1])
check_duplicates3([1, 6, 3, 5, 7, 3, 2, 1])

# Exercise 4
# Given an array, rotate the array to the right by k steps, where k is non-negative.

# Solutions


def rotate_array(array, k):
    sub_array_end = array[-3:]
    sub_array = array[0:-3]
    rotated_array = sub_array_end + sub_array
    print(rotated_array)
    return rotated_array


def rotate_array2(array = [1,2,3,4,5,6,7,8], k = 3):
    for i in range(0,k):
        current_element = array[0]
        last_element = array[-1]
        for j in range(0, len(array) - 1):
            next_element = array[j+1]
            array[j+1] = current_element
            current_element = next_element
        array[0] = last_element

    print(array)
    return array

def rotate_array3(nums, k):
    l, r = 0, len(nums) - 1
    while l < r:
        nums[l], nums[r] = nums[r], nums[l]
        l += 1
        r -= 1

    l, r = 0, k - 1
    while l < r:
        nums[l], nums[r] = nums[r], nums[l]
        l += 1
        r -= 1

    l, r = k, len(nums) - 1
    while l < r:
        nums[l], nums[r] = nums[r], nums[l]
        l += 1
        r -= 1

    print(nums)

rotate_array([1,2,3,4,5,6,7,8], 3)
rotate_array2([1,2,3,4,5,6,7,8], 3)
rotate_array3([1,2,3,4,5,6,7,8], 3)


# Exercise 5
# Have the function LongestWord(sen) take the sen parameter being passed and return the longest word in the string.
# If there are two or more words that are the same length, return the first word from the string with that length.
# Ignore punctuation and assume sen will not be empty. Words may also contain numbers, for example "Hello world123 567"


# Solution

def longest_word(sen):
    if type(sen) is not str or len(sen.split()) <= 1:
        print("Invalid parameter passed")

    words_list = sen.split()
    longest_word = words_list[0]

    for word in words_list:
        if len(word) > len(longest_word):
            longest_word = word

    print(longest_word)
    return longest_word


longest_word("Hey my name is Luis!")
longest_word("This is the longest word!")