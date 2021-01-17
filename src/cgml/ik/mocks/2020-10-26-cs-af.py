# Libraries Included:
# Numpy, Scipy, Scikit, Pandas

print("Hello, world!")

''''

     <--- root
>>> 1 >>>>>>>
|  / \     ||
| 4>> 3    ||
|      \   ||
<<<<<<  2 <<<

copy_with_extras(root) => newRoot

TreeNode { value, left:TreeNode, right:TreeNode, exra:TreeNode }

copy_graph(node) => newNode

GraphNode { value, nodes:List<GraphNode> }

plan_my_courses(courses:List, list of dependencies:List<Pair>)

courses = e, q, m, p, c, h

deps    = p needs m 
          q needs p
          c needs p
          c needs q
          h needs e

output  = m,e,p,q,c,h


''''


def copy_with_extras(root):
    d1 = {}  # dCopy2Original
    visited = {}  # dOriginal2Copy

    def _copy(root):
        if root is None:
            return None
        if dOriginal2copy.get(root):
            return dOriginal2copy.get(root)
        rootCopy = TreeNode(root.value)
        dCopy2Original[rootCopy] = root
        dOriginal2Copy[root] = rootCopy

        rootCopy.left = _copy(root.left)
        rootCopy.right = _copy(root.right)
        rootCopy.extra = _copy(root.extra)
        return rootCopy

    rootCopy = _copy(root)

    for node in graph:  # O(V+E)
        if node not in visited:
            _copy()

    return rootCopy


def course_schedule(pairs):
    g = {}
    for pair in pairs:
        g[pair[0]] = g.get(pair[0], [])
        g[pair[0]].append(pair[1])

    def _ts(node):
        for v in g[node]:
            if v not in visited:
                visited.add(v)
                _ts(v)
        output = [node] + output

    output = []
    visited = set()
    for node in g:
        if node not in visited:
            visited.add(node)
            _ts(node)
    return output
