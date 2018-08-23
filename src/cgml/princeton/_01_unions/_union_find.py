'''
Dynamic connectivity.

Given a set of N objects:
- union: connect two objects
- find: is there path between two objects

Properties:
- Reflexive, Symmetric, Transitive

Connected components:
- Maximum set of objects that are mutually connected

'''

class UnionFind:
    def __init__(self, N):
        self.N = N
        #super().__init__(N)
        self.ids = [k for k in range(N)]

    def union(self, p:int, q:int):
        pass

    def find(self, p:int, q:int) -> bool:
        pass

    def count(self) -> bool: # of components
        pass