def bfs(graph,start,target):
    queue = [[start]]
    visited = set()
    while queue:
        path = queue.pop(0)
        node = path[-1]
        if node == target: return path
        if node in visited: continue
        visited.add(node)
        queue+=[list(path)+[adjacent] for adjacent in graph.get(node,[])]


result = bfs(graph = {
        '1': ['2', '3', '4'],
        '2': ['5', '6'],
        '5': ['9', '10'],
        '4': ['7', '8'],
        '7': ['11', '12']
        },
    start='1',
    target='12')

assert result == ['1', '4', '7', '12']