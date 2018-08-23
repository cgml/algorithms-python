class LinkedList:
    val = None
    next = None

    def __init__(self, val):
        self.val = val


class Stack:
    root, _size = None, 0

    def push(self, val):
        n, n.next, self._size = LinkedList(val), self.root, self._size + 1
        self.root = n

    def pop(self):
        if not self.root: return None
        result, self.root, self._size = self.root, self.root.next, self._size - 1
        return result.val

    def empty(self):
        return self.root is None

    def size(self):
        return self._size

s = Stack()
s.push("a")
s.push("b")
s.push("c")
s.push("d")
while not s.empty(): print(s.pop())


