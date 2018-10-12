class MinStack(object):
    def __init__(self):
        self.stack, self.m = [], [float('inf')]

    def push(self, x):
        self.stack.append(x)
        self.m.append(min(self.m[-1], x))

    def pop(self):
        self.m.pop()
        self.stack.pop()

    def top(self):
        return None if not self.stack else self.stack[-1]

    def getMin(self):
        return None if len(self.m) < 2 else self.m[-1]
