# Example of Memoization

# Unmemoized Version
def add_to_80(n):
    return n + 80

# Memoized Version
cache = {}
def memoized_add_too_80(n):
    if n in cache.keys():
        return cache[n]
    print('Long Timeee.....')
    cache[n] = n + 80
    return cache[n]


# Memoized Version of Fibonacci
cache = {}
def fibon_master(n):
    if n in cache.keys():
        return cache[n]
    else:
        if n < 2:
            return n
        return fibon_master(n - 1) + fibon_master(n - 2)

if __name__ == '__main__':
    print(fibon_master(7))