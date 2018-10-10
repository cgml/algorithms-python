# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    def serialize(self, root):
        q, result = [root], []
        while q:
            node = q.pop(0)
            result.append(None if not node else node.val)
            if not node: continue
            q += [node.left, node.right]
        while result and result[-1]: result.pop()  # cut off last Nones
        return ','.join([str(v) for v in result])

    def deserialize(self, data):
        data = data.split(',')
        if not data or data[0] == 'None': return None
        croot = TreeNode(int(data.pop(0)))
        clayer = [croot]
        while data:
            nlayer = []
            for node in clayer:
                if node is None: continue
                if data:
                    nv = data.pop(0)
                    node.left = None if nv == 'None' else TreeNode(int(nv))
                if data:
                    nv = data.pop(0)
                    node.right = None if nv == 'None' else TreeNode(int(nv))
                nlayer += [node.left, node.right]
            clayer = nlayer
        return croot
