# Making use of recursion to understand base cases and recursive cases.

counter = 0


def inception():
    global counter
    print(counter)
    if counter > 3:
        return 'Done'
    counter += 1
    return inception()


# print(inception())

# Exercises
# Find the factorial of a number making use of recursion and iteration
def find_factorial_iterative(number):
    answer = 1
    for i in range(1, number + 1):
        answer = answer * i
    print(answer)


def find_factorial_recursive(number):
    if number == 1:
        return 1
    print('Iteration # ' + str(number))
    print(number, number - 1)
    return number * find_factorial_recursive(number - 1)


# print(find_factorial_recursive(5))

# Exercises
# Find the index of a value in a fibonacci sequence
def find_index_fib_iterative(n):
    seq = [0, 1]
    for i in range(0, n):
        seq.append(seq[i] + seq[i+1])
    print(seq[-1])
    return seq[n]


def find_index_fib_recursive(n):
    if n < 2:
        return n
    print(n-1, n-2)
    return find_index_fib_recursive(n - 1) + find_index_fib_recursive(n - 2)

# print(find_index_fib_iterative(7))
# print(find_index_fib_recursive(7))


# Calculate sum of a list
def calculate_list_sum(values):
    if len(values) == 1:
        return values[0]
    return values[0] + calculate_list_sum(values[1:])


# print(calculate_list_sum([1, 2, 3, 4, 5]))


# Calculate Sum of list with inner lists
def calculate_values_sum(values):
    total = 0
    for element in values:
        if type(element) is list:
            total += calculate_values_sum(element)
        else:
            total += element
    return total


# print(calculate_values_sum([1, 2, [3, 4], [5, 6]]))

# Calculate factorial of a number
def calculate_factorial(num):
    if num == 1:
        return 1
    return num * calculate_factorial(num - 1)

# print(calculate_factorial(5))


# Fibonacci Sequence Recursive
def fibonacci(n):
    if n < 2:
        return n

    return fibonacci(n-1) + fibonacci(n-2)


print(fibonacci(7))


# Get the sum of all the digits of a number
def sum_digits(number):
    if number is float:
        return 'Number must be an integer'
    number = str(number)
    if len(number) == 1:
        return int(number)
    total = int(number[0]) + sum_digits(int(number[1:]))
    return total


print(sum_digits(345))


# Get the sum of all the positive integers of a number
def get_sum(number):
    if number == 1 or number == 0:
        return number
    return number + get_sum(number - 2)


print(get_sum(10))

# Get the result of 'a' to the power of 'b'

def get_power(a,b,iteration):
    if b == iteration:
        return a
    return a * get_power(a, b, iteration + 1)


print(get_power(3, 4, 1))
