class StackMin:
    s = []
    m = []

    def min(self):
        return self.m[-1] if len(self.m) > 0 else None

    def push(self,x):
        self.s.append(x)
        self.m.append(x if len(self.m) == 0 else min(x,self.m[-1]))
        return self

    def pop(self):
        self.m.pop()
        return self.s.pop()

    def peek(self):
        return self.s[-1] if len(self.s) > 0 else None

    def isEmpty(self):
        return len(self.s) == 0

sm = StackMin().push(4).push(5).push(10).push(3).push(2).push(1)
while not sm.isEmpty(): print(sm.min(), sm.pop(), sm.min())