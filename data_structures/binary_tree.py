class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def put_value(self, value):
        if self.root is None:
            self.root = Node(value)
            return

        vacant_node = self._find_vacant_spot()
        if not vacant_node.left:
            vacant_node.left = Node(value)
        else:
            vacant_node.right = Node(value)

    def print_tree(self):
        def print_node(node):
            if node is None:
                return
            print(node.value)
            print_node(node.left)
            print_node(node.right)

        print_node(self.root)

    def _find_vacant_spot(self):
        def find_spot(node):
            if node is None:
                return None

            if node.left is None or node.right is None:
                return node
            return find_spot(node.left) or find_spot(node.right)

        return find_spot(self.root)

    def search(self, value) -> Node:
        return self._search(value, self.root)

    def _search(self, value, node):
        if not node:
            return None

        if node.value == value:
            return node

        return self._search(value, node.left) or self._search(value, node.right)


binary_tree = BinaryTree()
binary_tree.put_value(1)
binary_tree.put_value(2)
binary_tree.put_value(3)
binary_tree.put_value(4)
binary_tree.put_value(5)
binary_tree.put_value(6)

binary_tree.print_tree()
print(binary_tree.search(3))