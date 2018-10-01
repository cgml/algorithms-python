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

'''
Sweep Line Algorithm to find all intersections of array of orthogonal lines on 2D plane

Process start / end points of horizontal lines as events to add / remove line point to BST O(n)
For each vertical line perform search range O(R + log n)

TC: O(n*(R+ logn)
+SC: O(n)

'''
import heapq
import matplotlib.pyplot as plt

class Node:
    def __init__(self, k, v):
        self.k, self.v, self.left, self.right = k, v, None, None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, k, v):
        if not self.root: self.root = Node(k,v)
        else: self.root = self._insert(self.root, k, v)

    def _insert(self, node, k, v):
        if node is None: return Node(k,v)
        if node.k > k: node.left = self._insert(node.left, k, v)
        elif node.k < k: node.right = self._insert(node.right, k, v)
        return node

    def delete(self, k):
        if not self.root or self.root.k == k: self.root = None
        else: self.root = self._delete(self.root, k)

    def _delete(self, node, k):
        if node is None: return None
        if node.k == k:
            if not node.left: return node.right
            if not node.right: return node.left
            rm = node.left
            while rm.right: rm = rm.right
            node.k, node.v = rm.k, rm.v
            node.left = self._delete(node.left,rm.k)
            return node
        elif node.k > k: node.left = self._delete(node.left, k)
        else: node.right = self._delete(node.right,k)

    def range_search(self, lo, hi):
        result = []
        self._range_search(self.root, lo, hi, result)
        return result

    def _range_search(self, node, lo, hi, result):
        if node is None: return
        if node.k >= lo and node.k <= hi: result.append(node)
        if node.k > lo: self._range_search(node.left, lo, hi, result)
        if node.k < hi: self._range_search(node.right, lo, hi, result)

def sweep_line(vlines, hlines):
    q, bst = [], BST()
    for item in hlines:
        x1, y1, x2, y2 = item
        heapq.heappush(q, (x1,'hs',item))
        heapq.heappush(q, (x2,'he',item))
    for item in vlines:
        x1, y1, x2, y2 = item
        heapq.heappush(q, (x1, 'v', item))
    intersections = []
    while q:
        hpoint, op, item = heapq.heappop(q)
        x1, y1, x2, y2 = item
        if op == 'hs': bst.insert(y1, item)
        elif op == 'he': bst.delete(y1)
        elif op == 'v':
            result = bst.range_search(y1,y2)
            for r in result: intersections.append((item, r.v))
    return intersections

bst = BST()
import random
random.seed(17)
vlines = []
for i in range(100):
    h1 = random.randint(0,100)
    v1 = random.randint(0,100)
    v2 = random.randint(0,20)
    vlines.append((h1, v1, h1, v1+v2))

hlines = []
for i in range(100):
    v1 = random.randint(0,100)
    h1 = random.randint(0,100)
    h2 = random.randint(0,20)
    hlines.append((h1, v1, h1+h2, v1))

result = sweep_line(vlines,hlines)
plt.hlines([hlines])
for item in result:
    vl, hl = item
    print('Iter-section: ({}x{}), H:{}, V:{}'.format(vl[0],hl[1], item[1], item[0]))