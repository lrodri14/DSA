# Linked List Implementation

class Node:

    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:

    def __init__(self, value):
        node = Node(value)
        self.head = node
        self.tail = self.head
        self.length = 1

    def append(self, value):
        node = Node(value)
        self.tail.next = node
        self.tail = node
        self.length += 1

    def prepend(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node
        self.length += 1

    def call_alternative_method(self, index, node):
        if index == self.length:
            self.append(node)
            return True
        if index == 0:
            self.prepend(node)
            return True

    def traverse_content(self, index):
        if 1 <= index < self.length:
            current_element = self.head
            previous_element = self.head
            for i in range(0, index):
                previous_element = current_element
                current_element = current_element.next
            return current_element, previous_element

    def insert(self, index, value):
        node = Node(value)
        if self.call_alternative_method(index, node):
            return
        current_element, previous_element = self.traverse_content(index)
        node.next = current_element
        previous_element.next = node
        self.length += 1

    def remove(self, index):
        current_element, previous_element = self.traverse_content(index)
        previous_element.next = current_element.next
        del(current_element)

    [16,1,10,8]

    def reverse(self):
        if self.head.next is None:
            return self.head.next

        prev = None
        current = self.head
        self.tail = current

        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next

        self.head = prev

    def read_content(self):
        current_element = self.head
        while current_element:
            print(current_element.value)
            current_element = current_element.next


linkedList = LinkedList(10)
linkedList.append(8)
linkedList.prepend(16)
linkedList.insert(1, 1)
linkedList.reverse()
linkedList.read_content()


# Linked List Implementation

class DoubleLinkedNode:

    def __init__(self, value):
        self.value = value
        self.previous = None
        self.next = None


class DoubleLinkedList:

    def __init__(self, value):
        node = DoubleLinkedNode(value)
        self.head = node
        self.tail = self.head
        self.length = 1

    def append(self, value):
        node = DoubleLinkedNode(value)
        self.tail.next = node
        node.previous = node
        self.tail = node
        self.length += 1

    def prepend(self, value):
        node = DoubleLinkedNode(value)
        node.next = self.head
        self.head.previous = node
        self.head = node
        self.length += 1

    def call_alternative_method(self, index, node):
        if index == self.length:
            self.append(node)
            return True
        if index == 0:
            self.prepend(node)
            return True

    def traverse_content(self, index):
        if 1 <= index < self.length:
            current_element = self.head
            for i in range(0, index):
                current_element = current_element.next
            return current_element

    def insert(self, index, value):
        node = Node(value)
        if self.call_alternative_method(index, node):
            return
        current_element = self.traverse_content(index)
        node.next = current_element
        node.previous = current_element.previous
        node.previous.next = node
        current_element.previous = node
        self.length += 1

    def remove(self, index):
        current_element = self.traverse_content(index)
        current_element.previous.next = current_element.next
        current_element.next.previous = current_element.previous
        del(current_element)
        self.length -= 1

    def read_content(self):
        current_element = self.head
        while current_element:
            print(current_element.value)
            current_element = current_element.next


# doubleLinkedList = DoubleLinkedList(10)
# doubleLinkedList.append(8)
# doubleLinkedList.prepend(16)
# doubleLinkedList.insert(1, 1)
# doubleLinkedList.remove(2)
# doubleLinkedList.read_content()