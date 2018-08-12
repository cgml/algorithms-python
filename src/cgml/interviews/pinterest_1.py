#         7
#       / | \
#      3 11 9
#     /    / \
#    5     7 12
#
# output: {"7":[{"3":["5":[]]},{"11":[]},{"9":[{"7":[],"12":[]}]}]}

assert serialize(deserialize("{7,3,5,#,#,11,#,9,7,#,12,#,#,#}")) == "{7,3,5,#,#,11,#,9,7,#,12,#,#,#}"

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

