"""
Simple LinkedList implementation, according to Udacity Data Structures and Algorithms in Python course.
"""


class Node(object):
    """
    Node object that models a node in LinkedList, LinkedLists essentially a  graph that has unbalanced branches.
    it can's a value the LinkedList stores and a reference to next link.
    """

    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList(object):
    """
    LinkedList data structure that organizes a collection of data by linking one data to another.
    """

    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def append(self, value):
        """Insert a value at the end of the linked list, if the list is empty value is inserted as a first node."""
        node = Node(value)
        if self.is_empty():
            self._head = node
            self._tail = node
        else:
            self._tail.next = node
            self._tail = node
        self._size += 1

    def is_empty(self):
        return self._size == 0

    def insert(self, position, value):
        """Insert a value to a specified position."""
        if self._is_invalid_range(position):
            raise self._value_error()

        node = Node(value)
        if self._is_in_start(position):
            self._insert_to_start(node)
        elif self._is_in_middle(position):
            self._insert_to_middle(node, position)
        else:
            self._insert_to_end(node)

    def _is_in_start(self, position):
        return position == 0

    def _is_in_middle(self, position):
        return 0 < position < self._size - 1

    def _is_in_end(self, position):
        return position == self._size - 1

    def _insert_to_start(self, node):
        if self._head:
            temp = self._head
            self._head = node
            node.next = temp
            self._size += 1
        else:
            self.append(node.value)

    def _insert_to_middle(self, position, node):
        previous = None
        current = self._head
        index = 0
        while current:
            if index == position:
                temp = previous.next
                previous.next = node
                node.next = temp
                self._size += 1
                break
            previous = current
            current = current.next
            index += 1

    def _insert_to_end(self, node):
        self.append(node.value)

    def remove(self, position):
        """Remove a value to a specified position."""
        if self._is_invalid_range(position):
            raise self._value_error()

        if self._is_in_start(position):
            self._remove_from_start()
        elif self._is_in_middle(position):
            self._remove_from_middle(position)
        else:
            self._remove_from_end()

    def _remove_from_start(self):
        self._head = self._head.next
        self._size -= 1

    def _remove_from_middle(self, position):
        previous = None
        current = self._head
        index = 0
        while current:
            if index == position:
                previous.next = current.next
                self._size -= 1
                break
            previous = current
            current = current.next
            index += 1

    def _remove_from_end(self):
        previous = None
        current = self._head
        while current:
            previous = current
            current = current.next

            if current == self._tail:
                break

        if previous:
            previous.next = None
            self._tail = previous
            self._size -= 1

    def _value_error(self):
        return ValueError(f'Invalid range, max length is {self._size}.')

    def _is_invalid_range(self, position):
        return position < 0 or position > self._size

    def print(self):
        result = []
        current = self._head
        while current:
            result.append(current.value)
            current = current.next
        print(result)

    def size(self):
        return self._size


linked_list = LinkedList()
linked_list.append('a')
linked_list.append('b')
linked_list.append('c')
linked_list.append('d')
linked_list.insert(0, 'd')
linked_list.insert(0, 'c')
linked_list.insert(0, 'f')
linked_list.remove(0)
linked_list.remove(0)
linked_list.print()
