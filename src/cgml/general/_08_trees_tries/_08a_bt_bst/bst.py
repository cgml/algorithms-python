class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, k):
        if self.root is None: self.root = Node(k)
        else: self._insert(self.root, k)

    def _insert(self, root, k):
        if root.val < k:
            if root.right is None: root.right = Node(k)
            else: self._insert(root.right,k)
        else:
            if root.left is None: root.left = Node(k)
            else: self._insert(root.left, k)

    def get_prev_next(self, k):
        def _prev_next(root, key):
            if root is None: return
            # If key is present at root
            if root.val == key:
                # the maximum value in left subtree is predecessor
                if root.left:
                    tmp = root.left
                    while tmp.right: tmp = tmp.right
                    _prev_next.pre = tmp
                # the minimum value in right subtree is successor
                if root.right:
                    tmp = root.right
                    while tmp.left: tmp = tmp.left
                    _prev_next.nxt = tmp
            # If key is smaller than root's key, go to left subtree
            elif root.val > key:
                _prev_next.nxt = root
                _prev_next(root.left, key)
            else:# go to right subtree
                _prev_next.pre = root
                _prev_next(root.right, key)

        _prev_next.pre = None
        _prev_next.nxt = None
        _prev_next(self.root,k)

        return (None if not _prev_next.pre else _prev_next.pre.val,
                None if not _prev_next.nxt else _prev_next.nxt.val)

    def delete(self, k):
        self.root = self._delete(self.root, k)

    def _delete(self, root, key):
        if not root: return root
        if root.val > key: root.left = self._delete(root.left, key)
        elif root.val < key: root.right = self._delete(root.right, key)
        else:
            if not root.left: return root.right
            elif not root.right: return root.left
            else:
                successor = root.right
                while successor.left: successor = successor.left

                root.val = successor.val
                root.right = self._delete(root.right, successor.val)

        return root

    def search(self, k):
        return self._search(self.root, k)

    def _search(self, root, k):
        if root is None or root.val == k: return root
        return self._search(root.right, k) if root.val < k else self._search(root.left, k)

    def print(self):
        self._inorder(self.root)

    def _inorder(self,root):
        if root:
            self._inorder(root.left)
            print(root.val)
            self._inorder(root.right)

'''
              50
           /     \
          30      70
         /  \    /  \
       20   40  60   80
      15  35  45
     10  33 

'''
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