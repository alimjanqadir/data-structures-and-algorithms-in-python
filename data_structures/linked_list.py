class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList(object):
    def __init__(self):
        self.list = []
        self.head = None

    def append(self, node):
        node = Node(node.value)
        if self.head:
            current = self.head
            while current.next:
                current = current.next
            current.next = node
        else:
            self.head = node

    def insert(self, position, node):
        node = Node(node.value)
        if self.head:
            current = self.head
            index = 0
            while current.next:
                if index == position:
                    if current == self.head:
                        node.next = current
                        self.head = node
                    else:
                        node.next = current.next
                        current.next = node
                    break
                current = current.next
                index += 1
        else:
            self.head = node

    def delete(self, position):
        temp = self.list[position]
        previous_node_index = position - 1
        if position == self.head:
            del self.list[position]
        else:
            previous_node = self.list[previous_node_index]
            previous_node.next = temp.next
            del self.list[position]

    def print(self):
        result = []
        node = self.head
        while node:
            result.append(node.value)
            node = node.next
        print(result)


a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')

linked_list = LinkedList()
linked_list.append(a)
linked_list.append(b)
linked_list.append(c)
linked_list.insert(0, d)
linked_list.insert(0, d)
linked_list.insert(0, d)
linked_list.insert(0, d)
linked_list.insert(1, a)
linked_list.insert(1, a)
linked_list.insert(1, a)
linked_list.insert(0, b)
linked_list.insert(0, b)
linked_list.delete(0)
linked_list.delete(0)
linked_list.print()
