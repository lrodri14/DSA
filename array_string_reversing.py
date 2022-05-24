# Create a function that accepts a string and reverses it

# My Solution
def reverse_string(chars):
    chars_array = list(chars)
    reversed_string = ''
    for i in range(0,len(chars_array)):
        chars_array.insert(i, chars_array[-1])
        chars_array.pop()
        reversed_string += chars_array[i]
    print(reversed_string)


reverse_string("Luis")

# Other Solution
def reverse_string2(chars):
    # Start by checking your inputs
    if not chars or len(chars) < 2 or type(chars) is not str:
        return

    reversed_string = ''
    for i in range(len(chars) - 1, -1, -1):
        reversed_string += chars[i]

    print(reversed_string)


reverse_string2("Luis")


# Making use of built-in solutions
def reverse_string3(chars):
    print(chars[::-1])
    print("".join(reversed(chars)))

reverse_string3("Luis")