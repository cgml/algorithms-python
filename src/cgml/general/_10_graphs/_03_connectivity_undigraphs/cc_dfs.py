'''
Copyright 2018 Constantine Gurnov

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
documentation files (the "Software"), to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software,
and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included
in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED
TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE
OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
'''

import networkx as nx

class CCUGraph:
    def __init__(self, network):
        self.network, self.visited, self.ids, self.count = network, set(), {}, 0
        for v in network:
            if v in self.visited: continue
            self.dfs(v)
            self.count+=1

    def dfs(self, v1):
        if v1 in self.visited: return
        self.visited.add(v1)
        self.ids[v1]=self.count
        for v2 in self.network[v1]: self.dfs(v2)

    def connected(self, v1, v2):
        return self.ids[v1] == self.ids[v2]

    def components(self):
        return self.count

g = nx.Graph()
g.add_nodes_from('0123456789')
g.add_edges_from([
    ('0','1'),
    ('1','2'),
    ('3','4'),
    ('4','5'),
    ('6','7')
])

cc = CCUGraph(g)
assert cc.components() == 5
assert cc.connected('0','2')
assert not cc.connected('0','3')
assert not cc.connected('8','9')