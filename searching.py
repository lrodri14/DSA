# Binary Search Tree Searching Traversal

class Node:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:

    def __init__(self):
        self.root = None

    def lookup(self, value):
        if self.root is None:
            return False
        else:
            current_node = self.root
            while current_node:
                if value > current_node.value:
                    current_node = current_node.right
                elif value < current_node.value:
                    current_node = current_node.left
                else:
                    print("Value has been found", current_node.value)
                    return current_node.value

    def insert(self, value):
        node = Node(value)
        if self.root is None:
            self.root = node
        else:
            current_node = self.root
            while True:
                if value < current_node.value:
                    # Left
                    if current_node.left is None:
                        current_node.left = node
                        return
                    else:
                        current_node = current_node.left
                else:
                    # Right
                    if current_node.right is None:
                        current_node.right = node
                        return
                    else:
                        current_node = current_node.right

    def traverse_tree_level_order(self):
        if self.root is None:
            return
        element_queue = []
        element_queue.append(self.root)
        while len(element_queue) != 0:
            current = element_queue[0]
            print(current.value)
            if current.left is not None:
                element_queue.append(current.left)
            if current.right is not None:
                element_queue.append(current.right)
            element_queue.pop(0)

    def traverse_tree_level_order_r(self, queue, array):
        if self.root is None:
            return
        if len(queue) == 0:
            return array
        current_node = queue.pop(0)
        array.append(current_node.value)
        if current_node.left:
            queue.append(current_node.left)
        if current_node.right:
            queue.append(current_node.right)
        return self.traverse_tree_level_order_r(queue, array)

    def traverse_tree_preorder(self, node):
        if node is None:
            return
        print(node.value)
        self.traverse_tree_preorder(node.left)
        self.traverse_tree_preorder(node.right)

    def traverse_tree_inorder(self, node):
        if node is None:
            return
        self.traverse_tree_inorder(node.left)
        print(node.value)
        self.traverse_tree_inorder(node.right)

    def traverse_tree_postorder(self, node):
        if node is None:
            return
        self.traverse_tree_postorder(node.left)
        self.traverse_tree_postorder(node.right)
        print(node.value)

    def remove(self, value):
        if self.root is None:
            return

        current_node = self.root
        parent_node = None

        while current_node:
            if value < current_node.value:
                parent_node = current_node
                current_node = current_node.left
            elif value > current_node.value:
                parent_node = current_node
                current_node = current_node.right
            else:
                # Case 1: Leaf Node
                if current_node.left is None and current_node.right is None:
                    # Case 1.1: Node to be deleted is root node and empty binary tree
                    if parent_node is None:
                        self.root = None
                    # Case 1.2: If the deleted item is smaller than it's parent it means we are deleted a left child,
                    # parent.left must aim to None now
                    elif parent_node.value > current_node.value:
                        parent_node.left = None
                    # Case 1.3: If the deleted item is larger than it's parent it means we are deleted a right child,
                    # parent.right must aim to None now
                    else:
                        parent_node.right = None
                    del current_node
                    return
                # Case 2: We have an element with a single child, left child only
                elif current_node.right is None:
                    # Case 2.1: Node to be deleted is root node
                    if parent_node is None:
                        self.root = self.root.left
                    # Case 2.2: Node to be deleted is not root node
                    else:
                        parent_node.left = current_node.left
                    del current_node
                    return
                # Case 3: We have an element with a single child, right child only
                elif current_node.left is None:
                    # Case 3.1: Node to be deleted is root node
                    if parent_node is None:
                        self.root = self.root.right
                    # Case 3.2: Node to be deleted is not root node
                    else:
                        parent_node.right = current_node.right
                    del current_node
                    return
                # Case 4: We have an element with two children, left and right
                else:
                    substitute = current_node.right
                    substitute_parent = None

                    while substitute.left:
                        substitute_parent = substitute
                        substitute = substitute.left

                    # Case 4.1: Element to be deleted is root node
                    if parent_node is None:
                        # Case 4.1.1: Substitute has a parent node
                        if substitute_parent is not None:
                            substitute.left = self.root.left
                            substitute.right = self.root.right
                            substitute_parent.left = None
                        # Case 4.1.2: Substitute does not have a parent
                        else:
                            substitute.left = self.root.left
                        self.root = substitute
                        del current_node
                        return
                    # Case 4.2: Element to be deleted is not root node
                    else:
                        # Case 4.2.1: Substitute has a parent node
                        if substitute_parent is not None:
                            substitute.left = current_node.left
                            substitute.right = current_node.right
                            substitute_parent.left = None
                        # Case 4.2.2: Substitute does not have a parent
                        else:
                            substitute.left = current_node.left
                        if substitute.value < parent_node.value:
                            parent_node.left = substitute
                        else:
                            parent_node.right = substitute
                        del current_node
                        return

# tree = BinarySearchTree()
# tree.insert(77)
# tree.insert(55)
# tree.insert(89)
# tree.insert(12)
# tree.insert(34)
# tree.insert(56)
# tree.insert(78)
# tree.insert(97)
# tree.insert(100)
# tree.insert(32)
# tree.insert(75)
# tree.insert(98)
# tree.insert(43)
# tree.insert(21)
# tree.insert(92)
# print(tree.traverse_tree_level_order_r([tree.root], []))

# Graph Searching Traversal
