'''
1D intervals:
    - insert interval
    - search for interval
    - delete interval
    - interval intersection query

Solution: Interval Search Tree
    - two components at each node A, B, C
    - A: left endpoint as binary search tree key
    - B: right endpoint
    - C: max endpoint subtree rooted at a node

'''

class OneDIntervalAPI:
    def put(self, lo, hi, value):
        pass

    def get(self, lo, hi) -> object:
        pass

    def delete(self, lo, hi):
        pass

    def intersects(self, lo, hi) -> list:
        pass


