from collections import deque

def find_order(words):
    g = {}
    for w in words:
        for c in w:
            g[c]=set()
    for i in range(len(words)-1):
        for c1, c2 in zip(words[i],words[i+1]):
            if c1 != c2:
                g[c1].add(c2)
                break
    visited, ordered = set(), deque([])
    def tsort(n):
        if n in visited: return
        visited.add(n)
        for v1 in g[n]:
            if v1 in visited: continue
            tsort(v1)
            ordered.appendleft(v1)
    for v in g:
        if v in visited: continue
        tsort(v)
        ordered.appendleft(v)
    return ''.join(list(ordered))
