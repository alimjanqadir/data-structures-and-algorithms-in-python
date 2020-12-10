class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.list = []
        self.head = 0
        self.tail = 0

    def insert(self):
        pass

    def remove(self):
        pass

    def print_list(self):
        pass


a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
a.next = b
b.next = c
a.next = b
a.next = b
