'''
BST is Binary Tree in symmetric order

BST as symbol table:
    - every node has key & value
    - smaller keys are left, bigger keys are right

'''

class TreeNode:
    def __init__(self, k, v):
        self.k, self.v = k, v
        self.right = None
        self.left = None
