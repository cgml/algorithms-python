from collections import deque
# Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

class Solution:
    def getNode(self, mem, node_label):
        if mem.get(node_label) is None: mem[node_label] = UndirectedGraphNode(node_label)
        return mem[node_label]

    def cloneGraph(self, node):
        if node is None: return None
        queue, mem = deque([node]), dict()

        while queue:
            entry = queue.popleft()
            cloned_node = self.getNode(mem, entry.label)
            if not cloned_node.neighbors:
                for vertex in entry.neighbors:
                    vertex_clone = self.getNode(mem, vertex.label)
                    cloned_node.neighbors.append(vertex_clone)
                    queue.append(vertex)
        return mem[node.label]