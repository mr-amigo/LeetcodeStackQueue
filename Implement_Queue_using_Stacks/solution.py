class Node:
    def __init__(self, val, next=None):
        self.data = val
        self.next = next

class Stack:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def push(self, item):
        self.head = Node(item, self.head)

    def pop(self):
        if self.is_empty():
            return None

        result = self.head.data
        self.head = self.head.next
        return result

    def peek(self):
        if self.is_empty():
            return None
        return self.head.data


    def __str__(self):
        if self.is_empty():
            return 'Stack is empty'

        result = ''
        cur = self.head
        while cur.next is not None:
            result += str(cur.data) + ' -> '
            cur = cur.next
        result += str(cur.data)
        return result

    def __len__(self):
        if self.is_empty():
            return 0

        cur = self.head
        counter = 0
        while cur is not None:
            counter += 1
            cur = cur.next
        return counter


class MyQueue(object):
    def __init__(self):
        self.s1 = Stack()
        self.s2 = Stack()

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.s1.push(x)


    def pop(self):
        """
        :rtype: int
        """
        if self.s2.is_empty():
            while not self.s1.is_empty():
                self.s2.push(self.s1.pop())
        return self.s2.pop()

    def peek(self):
        """
        :rtype: int
        """
        if self.s2.is_empty():
            while not self.s1.is_empty():
                self.s2.push(self.s1.pop())
        return self.s2.peek()


    def empty(self):
        """
        :rtype: bool
        """
        return self.s1.is_empty() and self.s2.is_empty()



# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
