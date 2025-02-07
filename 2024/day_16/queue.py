class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, value):
        n = Node(value)
        if self.tail:
            self.tail.next = n
            self.tail = n
        else:
            self.head = n
            self.tail = n

    def dequeue(self):
        old = self.head
        self.head = self.head.next
        if self.head:
            old.next = None
        else:
            self.tail = None
        return old.value

    def print(self):
        el = self.head
        while el:
            print(el.value)
            el = el.next
        print("")    



def test_q():
    q = Queue()
    q.enqueue(4)
    q.enqueue(5)
    q.enqueue(6)
    q.print()
    q.dequeue()
    q.print()
    q.dequeue()
    q.print()
    q.enqueue(7)
    q.print()
    q.dequeue()
    q.dequeue()
    q.print()

