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

class FreqStack(object):
    def __init__(self):
        self.freq = {}
        self.group = {}
        self.max_freq = 0

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        f = self.freq.get(val, 0) + 1
        self.freq[val] = f
        self.max_freq = max(f, self.max_freq)
        if f not in self.group:
            self.group[f] = Stack()
        self.group[f].push(val)

    def pop(self):
        """
        :rtype: int
        """
        val = self.group[self.max_freq].pop()
        self.freq[val] -= 1
        if self.group[self.max_freq].is_empty():
            self.max_freq -= 1
        return val
