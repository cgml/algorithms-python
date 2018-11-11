'''
BST: prev / next / range
'''

class Node():
    def __init__(self, key):
        self.key = key
        self.right, self.left = None, None

    def __str__(self): return str(self.key)
    def __repr__(self): return str(self.key)

class BST():
    def __init__(self):
        self.root = None

    def _insert(self, node, key):
        if node is None: return Node(key)
        if node.key > key: node.left = self._insert(node.left, key)
        elif node.key < key: node.right = self._insert(node.right, key)
        return node

    def insert(self, key):
        if not self.root: self.root = Node(key)
        else: self.root = self._insert(self.root, key)

    def get_prev_next(self, key):
        def _prev_next(node, key):
            if node is None: return None
            if node.key == key:
                #the max value in left subtree is predecessor
                if node.left:
                    tmp = node.left
                    while tmp.right: tmp = tmp.right
                    _prev_next.prev = tmp
                #the min value in right subtree is successor
                if node.right:
                    tmp = node.right
                    while tmp.left: tmp = tmp.left
                    _prev_next.next = tmp
            #if key is smaller than node's key, go to left subtree
            elif node.key > key:
                _prev_next.next = node
                _prev_next(node.left, key)
            #if key is greater than node's key, go to right subtree
            else:
                _prev_next.prev = node
                _prev_next(node.right, key)
        _prev_next.prev, _prev_next.next = None, None
        _prev_next(self.root, key)
        return _prev_next.prev, _prev_next.next


    def search(self, key):
        def _search(node, key):
            if not node: return None
            if node.key == key: return node
            elif node.key > key: return _search(node.left, key)
            else: return _search(node.right, key)
        return _search(self.root, key)

    def delete(self, key):
        def _delete(node, key):
            if not node: return None
            if node.key > key: node.left = _delete(node.left, key)
            elif node.key < key: node.right = _delete(node.right, key)
            else:
                if not node.left: return node.right
                elif not node.right: return node.left
                else:
                    successor = node.right
                    while successor.left: successor = successor.left
                    node.key = successor.key
                    node.right = _delete(node.right, successor.key)

            return node

        self.root = _delete(self.root, key)


bst = BST()
bst.insert(50)
bst.insert(30)
bst.insert(20)
bst.insert(40)
bst.insert(70)
bst.insert(60)
bst.insert(80)
bst.insert(25)
bst.insert(10)
bst.insert(45)
bst.insert(35)
bst.insert(33)

print(bst.get_prev_next(45))
print(bst.get_prev_next(35))
print(bst.delete(50))
print(bst.get_prev_next(45))
print(bst.search(45))
print(bst.search(46))
