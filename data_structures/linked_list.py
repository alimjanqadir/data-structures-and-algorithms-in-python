class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, node):
        node = Node(node.value)
        if self.size:
            self.tail.next = node
            self.tail = node
        else:
            self.head = node
            self.tail = node
        self.size += 1

    def insert(self, position, node):
        if position < 0 or position > self.size:
            raise ValueError

        node = Node(node.value)
        current = self.head
        previous = None
        if current:
            index = 0
            while current:
                if index == position:
                    if position == 0:
                        node.next = current
                        self.head = node
                    elif position == self.size:
                        self.append(node)
                    else:
                        previous.next = node
                        node.next = current
                    self.size += 1
                    break
                previous = current
                current = current.next
                index += 1
            if current is None:
                self.append(node)
        else:
            self.head = node
            self.tail = node
            self.size += 1

    def delete(self, position):
        if position < 0 or position > self.size - 1:
            raise ValueError

        previous = None
        current = self.head
        index = 0
        while current:
            if index == position:
                if position == 0:
                    self.head = current.next
                elif position == self.size:
                    self.tail = previous
                else:
                    previous.next = current.next
                self.size -= 1
                break
            previous = current
            current = current.next
            index += 1

    def print(self):
        result = []
        current = self.head
        while current:
            result.append(current.value)
            current = current.next
        print(result)


a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')

linked_list = LinkedList()
linked_list.append(a)
linked_list.append(b)
linked_list.append(c)
linked_list.append(d)
linked_list.append(a)
linked_list.append(a)
linked_list.print()
