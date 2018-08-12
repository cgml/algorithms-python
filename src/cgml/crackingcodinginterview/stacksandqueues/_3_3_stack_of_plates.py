class StackOfStacks:
    ss = [[]]
    n = None

    def __init__(self,n):
        self.n=n

    def push(self,x):
        if len(self.ss[-1]) == self.n: self.ss.append([])
        self.ss[-1].append(x)
        return self

    def pop(self):
        if len(self.ss) == 1 and len(self.ss[-1])==0: return None
        x = self.ss[-1].pop()
        if len(self.ss[-1])==0: self.ss.pop()
        return x

    def pop_at(self,idx):
        if idx >= len(self.ss): return None
        x = self.ss[idx].pop()
        if len(self.ss[idx])==0 and idx>0: self.ss.pop(idx)
        return x

    def peek(self):
        if len(self.ss[-1])==0: return None
        return self.ss[-1][-1]

    def isEmpty(self):
        return len(self.ss)==1 and len(self.ss[-1])==0

ss = StackOfStacks(5)
for i in range(26): ss.push(i)
assert ss.pop_at(1) == 9
assert ss.pop_at(4) == 24