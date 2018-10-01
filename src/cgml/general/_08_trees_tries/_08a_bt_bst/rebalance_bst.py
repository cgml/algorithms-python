'''
Algorithm:
1. Create sorted array from BST with in-order traversal O(n)
2. Recursively create BST from sorted array O(n)

TC: O(n)
+SC: O(n)

'''

class Node:
    def __init__(self, k):
        self.key, self.left, self.right = k, None, None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if not self.root: self.root = Node(key)
        else: self.root = self._insert(self.root, key)

    def _insert(self, node, key):
        if node is None: return Node(key)
        if node.key > key: node.left = self._insert(node.left, key)
        elif node.key < key: node.right = self._insert(node.right, key)
        return node


    def traverse(self):
        result = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, node, result):
        if node is None: return
        self._inorder(node.left, result)
        result.append(node.key)
        self._inorder(node.right, result)

    def rebalance(self):
        result = self.traverse()
        self.root = self._rebalance(result)

    def _rebalance(self, array):
        if not array: return None
        midx = len(array) // 2
        root = Node(array[midx])
        root.left = self._rebalance(array[:midx])
        root.right = self._rebalance(array[midx+1:])
        return root

bst = BST()
for i in range(20): bst.insert(i)
bst.insert(-1)
print(bst.root.key,bst.root.left.key,bst.root.right.key)
bst.rebalance()
print(bst.root.key,bst.root.left.key,bst.root.right.key)
