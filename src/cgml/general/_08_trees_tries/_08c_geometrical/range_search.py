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

from collections import deque


class Node:
    def __init__(self, key, val=None):
        self.key, self.val, self.left, self.right, self.size = key, val, None, None, 0

    def __repr__(self): return "{}/{}".format(self.key, self.size)

    def __str__(self): return "{}/{}".format(self.key, self.size)


class RangeSearch:
    def __init__(self, root):
        self.root = root

    def find(self, key):
        return self._find(self.root, key)

    def _find(self, root, key):
        if not root: return None
        if root.key == key: return root
        return self._find(root.left, key) if root.key > key else self._find(root.right, key)

    def contains(self, key):
        return self.find(key) is not None

    def insert(self, key):
        if self.root is None: self.root, self.root.size = Node(key), 1
        else: self._insert(self.root, key)


    def _insert(self, root, key):
        if root.key < key:
            if root.right is None:
                root.right = Node(key)
                self._fix_size(root.right)
            else: self._insert(root.right, key)
        elif root.key > key:
            if root.left is None:
                root.left = Node(key)
                self._fix_size(root.left)
            else: self._insert(root.left, key)
        self._fix_size(root)

    def _fix_size(self, node):
        node.size = 1 + self._safe_size(node.left) + self._safe_size(node.right)

    def delete(self, key):
        #TODO
        pass

    def search_range(self, lo, hi):
        q = deque([])
        self._search_range(self.root, lo, hi, q)
        return list(q)

    def _search_range(self, root, lo, hi, q):
        if root is None: return
        if root.key >= lo: self._search_range(root.left, lo, hi, q)
        if root.key >= lo and root.key <= hi: q.append(root)
        if root.key <= hi: self._search_range(root.right, lo, hi, q)

    def range_count(self, lo, hi):
        if lo > hi: return 0
        if self.contains(hi): return 1 + self.rank(hi) - self.rank(lo)
        else: return self.rank(hi) - self.rank(lo)

    def min(self):
        key, c = None, self.root
        while c: key, c = c.key, c.left
        return key

    def max(self):
        key, c = None, self.root
        while c: key, c = c.key, c.right
        return key

    def size(self, key = None):
        if key is None: self._safe_size(self.root)
        else: return self._safe_size(self.find(key))

    def _safe_size(self, node):
        return 0 if node is None else node.size

    def rank(self, key):
        return self._rank(self.root, key)

    # Number of keys in Subtree less than key
    def _rank(self, root, key):
        if root is None: return 0
        if root.key > key: return self._rank(root.left, key)
        elif root.key < key: return 1 + self._safe_size(root.left) + self._rank(root.right, key)
        else: return self._safe_size(root.left)

bst = RangeSearch(Node(50))
for i in range(101)[::5]: bst.insert(i)
for i in range(101)[::2]: bst.insert(i)
# for i in range(100)[::5]: bst.insert(i)
# for i in range(100)[::2]: bst.insert(i)

print(bst.search_range(0,20))
print(bst.search_range(50,70))
print(bst.range_count(50,70))