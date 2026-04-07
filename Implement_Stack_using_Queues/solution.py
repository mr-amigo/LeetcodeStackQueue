class Node:
    def __init__(self, val, next=None):
        self.data = val
        self.next = next


class Queue:
    def __init__(self):
        self.head = None
        self.tail = self.head
        self._size = 0

    def is_empty(self):
        return self.head is None

    def add(self, item):
        new_node = Node(item)

        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        self._size += 1

    def pop(self):
        if self.is_empty():
            return None

        result = self.head.data
        self.head = self.head.next
        self._size -= 1

        if self.head is None:
            self.tail = None

        return result


    def peek(self):
        if self.is_empty():
            return None
        return self.head.data

    def __len__(self):
        return self._size

    def __str__(self):
        if self.is_empty():
            return 'Queue is empty'

        result = ''
        cur = self.head
        while cur.next is not None:
            result += str(cur.data) + ' -> '
            cur = cur.next
        result += str(cur.data)
        return result


class MyStack(object):
    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()


    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.q2.add(x)

        while not self.q1.is_empty():
            self.q2.add(self.q1.pop())

        self.q1, self.q2 = self.q2, self.q1


    def pop(self):
        """
        :rtype: int
        """
        return self.q1.pop()


    def top(self):
        """
        :rtype: int
        """
        return self.q1.peek()


    def empty(self):
        """
        :rtype: bool
        """
        return self.q1.is_empty() and self.q2.is_empty()



# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
