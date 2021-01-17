def minMultiplicationCost(s):
    mem = {}
    S = list(zip(s, s[1:]))

    def _min(i, j):
        if i == j:
            return 0
        if i + 1 == j:
            return S[i][0] * S[j][0] * S[j][1]
        key = '{}:{}'.format(i, j)
        if mem.get(key) is not None:
            return mem[key]
        c = float('inf')
        for k in range(i, j):
            cc = _min(i, k) + _min(k + 1, j) + S[i][0] * S[k + 1][0] * S[j][1]
            c = min(c, cc)
        mem[key] = c
        return c

    result = _min(0, len(S) - 1)
    return result
