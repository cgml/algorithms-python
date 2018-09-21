class Node:
    def __init__(self, val, data=None):
        self.val, self.data, self.right, self.left, self.red = val, data, None, None, False

class RBTree:
    def __init__(self):
        self.root = None

    def search(self, val, node=None):
        if self.root is None: return None
        if node is None: return self.search(self.root)
        if val == node.val: return node
        return self.search(val, self.root.left) if val > node.val else self.search(val, self.root.right)

    def _rotate_left(self, p, h, x):
        pass

    def _rotate_right(self, p, x, h):
        pass

    def _flip_colors(self, p, h, x):
        pass

    def insert(self, val, data=None):
        pass