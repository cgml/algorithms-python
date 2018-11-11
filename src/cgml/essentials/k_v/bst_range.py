from collections import deque

class Node():
    def __init__(self, k, v=None):
        self.key, self.val, self.cnt, self.left, self.right = k, v, 1, None, None

    def __repr__(self):
        return '{}'.format(self.key)

class RangeBST():
    def __init__(self):
        self.root = None

    def search(self, k):
        def _search(node, k):
            if not node: return None
            if node.key == k: return node
            else: return _search(node.left, k) if node.key > k else _search(node.right, k)
        if not self.root: return None
        else: return _search(self.root, k)

    def search_closest(self, k):
        p, n = self.get_prev_next(k)
        return p if not n or not p or abs(k - p.key) < abs(k - n.key) else n

    def search_range(self, lo, hi):
        q = deque([])
        def _search_range(node, lo, hi, q):
            if not node: return
            if node.key >= lo: _search_range(node.left, lo, hi, q)
            if node.key >= lo and node.key <= hi: q.append(node)
            if node.key <= hi: _search_range(node.right, lo, hi, q)
        _search_range(self.root, lo, hi, q)
        return list(q)

    def count_range(self, lo, hi):
        if lo > hi: return 0
        if self.search(hi) is not None: return 1 + self.rank(hi) - self.rank(lo)
        else: return self.rank(hi)-self.rank(lo)

    def _safe_size(self, node):
        return 0 if not node else node.cnt

    def rank(self, k=None):
        if not self.root: return 0
        def _rank(node, k):
            if node is None: return 0
            elif node.key > k: return _rank(node.left, k)
            elif node.key < k: return 1 + self._safe_size(node) + _rank(node.right, k)
            else: return self._safe_size(node.left)

        return _rank(self.root, self.root.key) if not k else _rank(self.root, k)

    def insert(self, k, v=None):
        def _insert(node, k, v):
            if not node: return
            if node.key == k: node.val = v
            elif node.key > k:
                if not node.left: node.left = Node(k,v)
                else: _insert(node.left, k, v)
            else:
                if not node.right: node.right = Node(k,v)
                else: _insert(node.right, k, v)
            self._update_cnt(node)
        if not self.root: self.root = Node(k,v)
        else: _insert(self.root, k, v)

    def remove(self, k):
        def _remove(node, k):
            if node.key == k:
                if not node.left: return node.right
                if not node.right: return node.left
                nxt = node.right
                while nxt.left: nxt = nxt.left
                node.key, node.val = nxt.key, nxt.val
                node.right = _remove(node.right, nxt.key)
            elif node.key > k: node.left = _remove(node.left, k)
            else: node.right = _remove(node.right, k)
            self._update_cnt(node)
            return node

        if self.root: self.root = _remove(self.root, k)

    def _update_cnt(self, node):
        if not node: return
        node.cnt = 1 + (0 if not node.right else node.right.cnt) + (0 if not node.left else node.left.cnt)

    def remove_range(self, low, high): # similar to remove operation in list
        pass

    def get_prev_next(self, k):
        def _prev_next(node, k):
            if not node: return
            if node.key == k:
                if node.left:
                    tmp = node.left
                    while tmp.right: tmp = tmp.right
                    _prev_next.prev = tmp
                if node.right:
                    tmp = node.right
                    while tmp.left: tmp = tmp.left
                    _prev_next.nxt = tmp
            elif node.key > k:
                _prev_next.nxt = node
                _prev_next(node.left, k)
            else:
                _prev_next.prev = node
                _prev_next(node.right, k)
        _prev_next.prev, _prev_next.nxt = None, None
        _prev_next(self.root, k)
        return _prev_next.prev, _prev_next.nxt

    def traversal(self):
        q = deque([])
        def _inorder(node, q):
            if not node: return
            _inorder(node.left,q)
            q.append(node.key)
            _inorder(node.right,q)
        _inorder(self.root, q)
        return list(q)


bst = RangeBST()
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
print(bst.traversal())
print(bst.search_range(10,80))
print(bst.remove(50))
print(bst.search_range(10,80))
print(bst.get_prev_next(45))
print(bst.search(45))
print(bst.search_closest(46))
print(bst.search_closest(54))

