# Array implementation in Python making use of Classes

# Array Class
class Array:

    # Constructor
    def __init__(self):
        self.length = 0
        self.data = {}

    # Get Element Method
    def get(self, index):
        value = self.data.get(index, 'Value not found')
        print(value)
        return value

    # Push Element Method
    def push(self, item):
        self.data[len(self.data)] = item
        self.length += 1

    # Pop Element Method
    def pop(self):
        self.length -= 1
        item = self.data.popitem()
        print(item)
        return item

    # Shift Items method
    def shift_items(self, index):
        for i in range(index, self.length):
            self.data[i] = self.data[i+1]
        self.data.popitem()
        print(self.data.values())


    # Delete Element Method
    def delete(self, index):
        item = self.data.get(index, 'Index not exisiting')
        self.data.pop(index)
        self.length -= 1
        self.shift_items(index)
        print(item)


# Making use of the Array Class
array = Array()

# Making use of the Get method
array.get(0)

# Making use of the Push Method
array.push(1)

# Corroborating the functionality of the Push Method with the Get method
array.get(0)

# Making use of the Pop Method, without an index
array.pop()

# Corroborating the functionality of the Get Method with the Get method
array.get(0)

# Making use of the Push Method
array.push(2)
array.push(3)
array.push(4)

# Making use of the Pop Method
array.delete(1)