class UGraph:
    nodes = {}

    def add(self, n1,n2):
        if self.nodes.get(n1) is None: self.nodes[n1] = Node(n1)
        if self.nodes.get(n2) is None: self.nodes[n2] = Node(n2)
        self.nodes.get(n1).connections[n2] = self.nodes.get(n2)
        self.nodes.get(n2).connections[n1] = self.nodes.get(n1)

    def __str__(self):
        return '\n'.join([''.join([str(k), ':', str(n)]) for k, n in self.nodes.items()])


class Node:
    value = None
    connections = None

    def __init__(self, value):
        self.value = value
        self.connections = {}

    def __str__(self):
        return ','.join([str(v) for v in self.connections.keys()])

class GraphUtils:
    @staticmethod
    def ugraph_from_list(l):
        result = UGraph()
        for (n1, n2) in l: result.add(n1, n2)
        return result


# print(GraphUtils.ugraph_from_list([(1,2),(1,3),(1,4),(3,4),(4,5)]))