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