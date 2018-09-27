'''
Copyright 2018 Constantine Gurnov

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
documentation files (the "Software"), to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software,
and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included
in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED
TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE
OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
'''

class Node:
    def __init__(self, key, data=None, red=False):
        self.key, self.data, self.right, self.left, self.size = key, data, None, None, 0
        # Color of PARENT link. can be checked as parent.left.red, parent.right.red
        self.red = red


class RBTree:
    def __init__(self):
        self.root = None

    def search(self, key):
        if self.root is None: return None
        return self._search(key, self.root)

    def _search(self, key, node):
        if node is None: return None
        if key == node.key: return node
        return self._search(key, node.left) if key < node.key else self._search(key, node.right)


    def red(self, n): return n is not None and n.red
    def contains(self, key): return self.search(key) is not None

    # def _safe_size(self, node): return 0 if not node else node.size
    # def size(self): return self._safe_size(self.root)

    def insert(self, key):
        self.root = self._insert(self.root, key)
        self.root.red = False

    def _insert(self, root, key):
        if root is None: return Node(key, red=True)

        if root.key > key: root.left = self._insert(root.left, key)
        elif root.key < key: root.right = self._insert(root.right, key)
        else: root.key = key # reassign data

        # fix ups
        # case 1: right red subtree => rotate to left
        if self.red(root.right) and not self.red(root.left): root = self._rotate_left(root)
        # case 2: 2 left reds in a row => rotate right, and then it becomes case 3
        if self.red(root.left) and self.red(root.left.left): root = self._rotate_right(root)
        # case 3: root became 4-node (left and right are reds) => flip
        if self.red(root.right) and self.red(root.left): root = self._flip_color(root)
        return root

    def _rotate_left(self, h):
        # maintains symmetric order and perfect black balance
        assert self.red(h.right) # we need to rotate left only red nodes
        x = h.right
        h.right = x.left
        x.left = h
        x.red = h.red
        h.red = True
        return x

    def _rotate_right(self, h):
        assert self.red(h.left)
        x = h.left
        h.left = x.right
        x.right = h
        x.red = h.red
        h.red = True
        return x

    def _flip_color(self, h):
        # recolor / split (temporary) 4-node
        assert not self.red(h)
        assert self.red(h.left)
        assert self.red(h.right)
        h.red, h.left.red, h.right.red = True, False, False
        return h


rbt = RBTree()
for i in range(100): rbt.insert(i)
print(rbt.root.key)
print(rbt.root.right.key)
print(rbt.root.left.key)
for i in range(100): assert rbt.contains(i)
