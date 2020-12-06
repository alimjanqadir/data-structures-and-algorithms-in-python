class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        self.preorder_insert(self.root, new_val)

    def preorder_insert(self, start, new_val):
        if start:
            if new_val < start.value:
                if start.left:
                    self.preorder_insert(start.left, new_val)
                else:
                    start.left = Node(new_val)
            else:
                if start.right:
                    self.preorder_insert(start.right, new_val)
                else:
                    start.right = Node(new_val)

    def print_tree(self):
        print self.preorder_print(self.root, "")

    def preorder_print(self, start, traversal):
        if start:
            traversal += str(start.value) + "-"
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal

    def search(self, find_val):
        return self.bst_search(self.root, find_val)

    def bst_search(self, start, find_val):
        if start:
            if find_val < start.value:
                return self.bst_search(start.left, find_val)
            elif find_val > start.value:
                return self.bst_search(start.right, find_val)
            else:
                return True
        return False


# Set up tree
tree = BST(4)

# Insert elements
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(5)

# Check search
# Should be True
print tree.search(4)
# Should be False
print tree.search(6)
