class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    """ Binary search tree that demonstrates its fundamental properties. To minimize the implementation we consider
    all inputs are different.
      """

    def __init__(self, value):
        self.root = Node(value)

    def print(self):
        def print_helper(node):
            """Recursive in order tree print helper. """
            if node is None:
                return

            print(node.value)
            print_helper(node.left)
            print_helper(node.right)

        """Prints the binary tree in pre-order fashion."""
        if self.root:
            print_helper(self.root)

    def insert(self, value):
        def insert_helper(node):
            """Recursive insert helper, inserts the value into the appropriate position."""
            if node is None:
                return node

            if value < node.value:
                if node.left is None:
                    node.left = Node(value)
                else:
                    insert_helper(node.left)
            else:
                if node.right is None:
                    node.right = Node(value)
                else:
                    insert_helper(node.right)

        """Inserts a node into the binary tree."""
        if self.root:
            insert_helper(self.root)
        else:
            self.root = Node(value)

    def search(self, value):
        def search_helper(node):
            if node is None:
                return None

            if value == node.value:
                return node
            elif value < node.value:
                return search_helper(node.left)
            else:
                return search_helper(node.right)

        """Traverse the binary tree and returns the first occurrence of the value."""

        if self.root == value:
            return self.root
        else:
            return search_helper(self.root)


# Some examples:
tree = BinarySearchTree(5)
tree.insert(10)
tree.insert(20)
tree.insert(30)

# Print
tree.print()

# Search
result = tree.search(30)
print(result.value)
