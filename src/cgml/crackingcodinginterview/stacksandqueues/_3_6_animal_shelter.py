# class Animal:
#     t = None
#
#     def __init__(self,t):
#         self.t=t
#
#     def __eq__(self, other):
#         return self.t == other.t
#
class LLNode:
    prev = None
    next = None
    data = None

    def __init__(self, t):
        self.data = t

class LL:
    tail = None
    head = None

    def add_head(self, n):
        if self.head is None: n.next, n.prev, self.head = None,None, n
        else: self.head.prev, self.head, n.prev, n.next = n, n, None, self.head

    def remove(self, n):
        if n is self.head and self.head.next is None: self.head = None
        elif n is self.head: self.head.next.prev, self.head = None, self.head.next
        else:
            c = self.head
            while c is not None and c is not n: c = c.next
            if c is None: return self
            c.prev.next = c.next

class AnimalShelter:
    ll = LL()
    qs = {'dog':[],'cat':[]}

    def push(self, t):
        self.ll.add_head(LLNode(t))
        self.qs[t].insert(0,self.ll.head)
        return self

    def pop_t(self,t):
        a=self.qs[t].pop()
        self.ll.remove(a)
        return a

    def pop(self):
        a=self.ll.tail
        self.ll.remove(a)
        return self.qs[a.data].pop()

    def print_all(self):
        c = self.ll.head
        while c is not None: print(c.data,end=' '); c=c.next

shelter = AnimalShelter()
for a in ['dog','cat','cat','cat','dog','dog']: shelter.push(a)

shelter.pop_t('cat')
shelter.pop_t('cat')
shelter.pop_t('dog')
shelter.print_all()