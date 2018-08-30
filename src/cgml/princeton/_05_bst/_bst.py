class Node:
    def __init__(self, v):
        self.val = v
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def _push_helper(self, root, k):
        if self.root is None:
            self.root = Node(k)
            return self.root

    def push(self, k):
        # if self.root is None:
        #     self.root = Node(k)
        #     return self.root
        # else:
        #     if k
        pass
        #TODO