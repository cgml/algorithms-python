from ._union_find import *

'''
Init: O(n)
Union: O(n)
Find: O(1)
'''
class QuickFind(UnionFind):

    def find(self, p:int, q:int) -> bool:
        return self.ids[p] == self.ids[q]

    def union(self, p:int, q:int):
        for idx in range(len(self.ids)):
            if self.ids[idx]==self.ids[q]:
                self.ids[idx]=self.ids[p]
