class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.list = []
        self.head = 0
        self.tail = 0

    def append(self, node):
        if len(self.list) > 0:
            temp = self.list[self.tail - 1]
            temp.next = node
        self.list.append(node)
        self.tail += 1

    def insert(self, position, node):
        if position < 0 or position > len(self.list) - 1 or node is None:
            return

        self.list.append(node)
        if position == self.head:
            temp = self.list[position]
            node.next = temp
            self.head = len(self.list) - 1
        else:
            temp = self.list[position]
            previous_node = self.list[position - 1]
            previous_node.next = node
            node.next = temp
        self.tail += 1

    def remove(self, position):
        if len(self.list) == 0 or position < 0 or position > len(self.list) - 1:
            return

        temp = self.list[position]
        previous_node_index = position - 1
        if position == self.head or position == self.tail:
            del self.list[position]
        else:
            previous_node = self.list[previous_node_index]
            previous_node.next = temp.next
            del self.list[position]
        self.tail -= 1

    def print_list(self):
        result = []
        list_index = 0
        node = self.list[self.head]
        while list_index < self.tail and node:
            result.append(node.value)
            node = node.next
            list_index += 1
        print(result)


a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')

linked_list = LinkedList()
linked_list.append(a)
linked_list.append(b)
linked_list.append(b)
linked_list.append(b)
linked_list.append(b)
linked_list.append(c)
linked_list.append(c)
linked_list.append(c)
linked_list.append(c)
linked_list.append(c)
linked_list.append(d)
linked_list.append(d)
linked_list.insert(0, d)
linked_list.insert(0, d)
linked_list.insert(0, d)
linked_list.insert(0, d)
linked_list.insert(0, d)
linked_list.insert(0, d)
linked_list.insert(0, d)
linked_list.print_list()
