# Return the recurrent element from an array, implement the solution using arrays and hash tables

# Array Solution

def recurrent_element(elements):
    if type(elements) is not list:
        return None

    if len(elements) <= 1:
        return elements

    checked_elements = []
    for i in elements:
        if i in checked_elements:
            return i
        else:
            checked_elements.append(i)

    if len(checked_elements) == len(elements):
        return None

    # This loops through all the array one by one, so it doesn't
    # detects recurrent elements that are closer to each
    # for i in range(0, len(elements)):
    #     for j in range(i+1, len(elements)):
    #         if elements[i] == elements[j]:
    #             return elements[i]

    return None


# Hash Table Solution

def recurrent_element_hash(elements):
    if type(elements) is not list:
        return None

    if len(elements) <= 1:
        return elements

    checked_elements = {}

    for i in elements:
        if checked_elements.get(i) is None:
            checked_elements[i] = 1
        else:
            return i

    return None


# Usage
print(recurrent_element([2, 1, 1, 2, 3, 5, 1, 2, 4]))
print(recurrent_element_hash([2, 1, 1, 2, 3, 5, 1, 2, 4]))
print(recurrent_element([2, 3, 4, 5]))
print(recurrent_element_hash([2, 3, 4, 5]))

