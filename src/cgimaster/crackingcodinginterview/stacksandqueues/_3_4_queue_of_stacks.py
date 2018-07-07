class MyQueue:
    sout, sin = [],[]

    def push(self,x):
        self.setinstate()
        self.sin.append(x)
        return self

    def pop(self):
        self.setoutstate()
        return self.sout.pop()

    def setinstate(self):
        while len(self.sout)>0: self.sin.append(self.sout.pop())

    def setoutstate(self):
        while len(self.sin)>0: self.sout.append(self.sin.pop())

    def isEmpty(self):
        return (len(self.sout) + len(self.sin))==0

q = MyQueue()
for i in range(20): q.push(i)
for i in range(20):assert i == q.pop()
