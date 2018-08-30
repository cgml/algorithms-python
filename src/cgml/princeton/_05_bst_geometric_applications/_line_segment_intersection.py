'''
Orthogonal line segment intersection search

Brute-force:
    compare all pairs for intersection - O(N^2)

Sweep line algorithm: optimized O(NlogN + R)
    sweep by x - coordinate
    left endpoint add y coordinates to BST,
    right endpoint remove y coordinate from BST
    when we hit vertical line - do range search on BST (any point found in BST represents intersection)


'''

