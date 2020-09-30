# Complete the function below.
from collections import deque


def string_transformation(words, start, stop):
    words = set(words)
    q = deque([(start, [])])
    while q:
        word, p = q.popleft()
        np = p + [word]
        if word == stop and len(np) > 1:
            return np
        lw = list(word)
        for idx in range(len(word)):
            cidx = lw[idx]
            for c in range(26):
                rc = chr(ord('a') + c)
                if rc == cidx: continue
                lw[idx] = rc
                w1 = ''.join(lw)
                if w1 == stop:
                    q.append((w1, np))
                if w1 in words:
                    q.append((w1, np))
                    words.remove(w1)
            lw[idx] = cidx
    return ["-1"]
