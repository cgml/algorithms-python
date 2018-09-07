#         7
#       / | \
#      3 11 9
#     /    / \
#    5     7 12
#
# output: {"7":[{"3":["5":[]]},{"11":[]},{"9":[{"7":[],"12":[]}]}]}

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def deserializeBT(s):
    if not s: return None
    a = s.split(',')
    if not str(a[0]).isnumeric(): return None
    root = TreeNode(int(a[0]))
    deserialize_bt(a,1,root)
    return root

def deserialize_bt(a,curidx,root):
    if curidx == len(a): return curidx
    if str(a[curidx]) == '#': curidx+=1
    elif str(a[curidx]).isnumeric():
        root.left = TreeNode(int(a[curidx]))
        curidx = deserialize_bt(a,curidx+1,root.left)
    else: raise Exception('Invalid Tree {}'.format(a[curidx]))
    if curidx < len(a):
        if str(a[curidx]) == '#': curidx+=1
        elif str(a[curidx]).isnumeric():
            root.right = TreeNode(int(a[curidx]))
            curidx = deserialize_bt(a,curidx+1,root.right)
        else: raise Exception('Invalid Tree {}'.format(a[curidx]))
    return curidx

def serializeBT(root):
    output = []
    serialize_bt(root,output)
    return ",".join(output[:-1])

def serialize_bt(root,output):
    if not root:
        output.append('#')
        return
    output.append(str(root.val))
    serialize_bt(root.left, output)
    serialize_bt(root.right, output)

assert serializeBT(deserializeBT("1,2,3,#,4,#,#,5,#,6,#,#")) == "1,2,3,#,4,#,#,5,#,6,#,#"

# N long(b)N
# b - expected(#) of nodes at each layer

# "", None =>

#  Tree -> dict -> format json
#  from json -> dict -> Tree
#  TC: O(N)
#  SC: O(N)
#
#
# class Node:
#     def __init__(self, val):
#         self.value = val
#         self.children = []
#
#
# def serialize(root):
#     return ",".join(serialize_helper(root)).replace("[,]", "[]")
#
#
# def serialize_helper(root):
#     if root is None: return []
#     nodes = [serialize_helper(node) for node in root.children]
#     result = ["{\"{}\":[".format(root.value), nodes, "]}"]  # nodes = ["{\"3\":["],"{\"5\":["],["]}","{\"11\":["],["]}",["]}"]
#     return result
#
#
# def deserialize(s):
#     if not s: return []
#     strips = s[1:-2]
#     value, current_nodes = strips[:strips.index(":")].replace("\"", ""), strips[strips.index(":") + 2:-2]  # 7, {"3":["5":[]]},{"11":[]},{"9":[{"7":[],"12":[]}]}
#     node = Node(value)
#     children = []
#     while current_nodes:
#         idx = find_closing_curvy_brakets(current_nodes)
#         node_str = current_nodes[:idx + 1]
#         children += [deserialize(node_str)]
#         if len(current_nodes) == idx + 1: current_nodes = None
#         else: current_nodes = current_nodes[idx + 2:]
#     node.children = children
#     return Node
#
#
# def find_closing_curvy_brakets(s):
#     queue = []
#     list_s = list(s)  # <--
#     queue.append(list_s.pop(0))
#     idx = 0
#     while list_s:
#         e = list_s.pop(0)
#         if e == "{": queue.append(e)
#         elif e == "}": queue.pop()
#         idx += 1
#     return idx
#
#
# assert "{\"7\":[{\"3\":{}}]}" == serialize(deserialize("{\"7\":[{\"3\":{}}]}"))

