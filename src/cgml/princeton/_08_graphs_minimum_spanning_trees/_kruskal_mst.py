'''
Kruskal's - 1956
Idea sort edges by weight
Add edges to tree unless it creates cycle (check fast with Union Find / connected component)

Time Complexity: O(log*V)
Space Complexity:
'''
from queue import PriorityQueue
from collections import deque

class KruskalMST:
    mst = None
    G = None

    def __init__(self, G):
        self.G = G

    def execute(self):
        self.mst = deque([])
        pq = PriorityQueue()
        for edge in self.G:
            pq.put(edge)


