# Stacks implementation using Arrays and Linked Lists

# Stack Implementation using Linked Lists

class Node:
    def __init__(self, value, next_element):
        self.value = value
        self.next = next_element


class Stack:
    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0

    def peek(self):
        print(self.top.value)

    def pop(self):
        popped_element = self.top
        self.top = self.top.next
        print(popped_element.value)
        del(popped_element)
        self.length -= 1

    def push(self, value):
        node = Node(value, self.top)

        if self.length == 0:
            self.top = node
            self.bottom = node

        if self.top is not None:
            self.top = node

        self.length += 1

    def is_empty(self):
        print(self.top is None)

# stack = Stack()
# stack.is_empty()
# stack.push(1)
# stack.push(2)
# stack.pop()
# stack.peek()
# stack.is_empty()

# Stack implementation using Arrays


class Stack:
    def __init__(self):
        self.list = []
        self.top = None
        self.bottom = None
        self.length = 0

    def pop(self):
        self.list.pop()
        self.top = self.list[-1]
        self.length -= 1

    def peek(self):
        print(self.top)

    def push(self, value):
        if self.top is None and self.bottom is None:
            self.top = value
            self.bottom = value
        else:
            self.top = value
        self.list.append(value)
        self.length += 1

    def is_empty(self):
        print(len(self.list) == 0)


# stack = Stack()
# stack.is_empty()
# stack.push(1)
# stack.push(2)
# stack.pop()
# stack.peek()
# stack.is_empty()

# Queues implementation using Arrays and Linked Lists

# Queue Implementation using Linked Lists

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def peek(self):
        print(self.first.value)

    def enqueue(self, value):
        node = Node(value)
        if self.length == 0:
            self.first = node
            self.last = node
        else:
            self.last.next = node

        self.length += 1

    def dequeue(self):
        first_element = self.first
        self.first = first_element.next
        del first_element
        self.length -= 1

    def is_empty(self):
        print(self.first is None)

    def read_content(self):
        current = self.first
        while current is not None:
            print(current.value)
            current = current.next


queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.dequeue()
queue.read_content()

