from data_structures.linked_list import LinkedList


class Stack(object):
    def __init__(self):
        self.linked_list = LinkedList()

    def push(self, value):
        self.linked_list.insert(0, value)

    def pop(self):
        head = self.linked_list._head.value
        self.linked_list.remove(0)
        return head

    def print(self):
        self.linked_list.print()


stack = Stack()
stack.push('a')
stack.push('b')
stack.push('c')
stack.push('d')
stack.push('e')
stack.print()
