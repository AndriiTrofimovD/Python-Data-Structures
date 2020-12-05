
class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def min_node(self):
        if self.left is not None:
            return self.left.min_node()
        return self


class BinaryTree:

    def __init__(self, root=None):
        if not root:
            self.root = root
        else:
            self.root = Node(root)

    @staticmethod
    def find_min(node):
        node = node.min_node()
        return node

    def insert(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            self._insert(self.root, value)

    def _insert(self, node, value):
        new_node = Node(value)
        if value < node.data:
            if not node.left:
                node.left = new_node
            else:
                self._insert(node.left, value)
        else:
            if not node.right:
                node.right = new_node
            else:
                self._insert(node.right, value)

    def remove(self, value):
        self.root = self._remove(self.root, value)

    def _remove(self, node, value):
        if not node:
            print(f'{value} is not in the tree.')
        elif value < node.data:
            node.left = self._remove(node.left, value)
        elif value > node.data:
            node.right = self._remove(node.right, value)
        else:
            if not node.left and not node.right:
                node = None
                return node
            elif not node.left:
                node = node.right
                return node
            elif not node.right:
                node = node.left
                return node
            else:
                min_right = self.find_min(node.right)
                node.data = min_right.data
                node.right = self._remove(node.right, node.data)
        return node

    def contains(self, value):
        if not self.root:
            return False
        return self._contains(self.root, value)

    def _contains(self, node, value):
        if value == node.data:
            return True
        elif value < node.data and node.left:
            return self._contains(node.left, value)
        elif value > node.data and node.right:
            return self._contains(node.right, value)
        else:
            return False

    def print_in_order(self):
        self._print_in_order(self.root)
        print()

    def _print_in_order(self, node):
        if node:
            self._print_in_order(node.left)
            print(node.data, end=" ")
            self._print_in_order(node.right)

    def print_post_order(self):
        self._print_post_order(self.root)
        print()

    def _print_post_order(self, node):
        if node:
            self._print_post_order(node.left)
            self._print_post_order(node.right)
            print(node.data, end=" ")

    def print_pre_order(self):
        self._print_pre_order(self.root)
        print()

    def _print_pre_order(self, node):
        if node:
            print(node.data, end=" ")
            self._print_pre_order(node.left)
            self._print_pre_order(node.right)
