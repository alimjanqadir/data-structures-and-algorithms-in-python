class Queue(object):

    def __init__(self):
        self.list = []

    def enqueue(self, value):
        self.list.append(value)

    def dequeue(self):
        if self.list:
            value = self.list[0]
            del self.list[0]
            return value

    def peek(self):
        if self.list:
            return self.list[0]
        return None

    def print(self):
        print(repr(self.list))


queue = Queue()
queue.enqueue('a')
queue.enqueue('b')
queue.enqueue('c')
queue.dequeue()
queue.print()
