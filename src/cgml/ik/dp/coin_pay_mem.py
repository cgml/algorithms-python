def maxWin(v):
    mem = {}
    def _max(si, ei):
        if si == ei:
            return v[si]
        key = '{}:{}'.format(si,ei)
        if mem.get(key) is not None:
            return mem[key]
        V = sum(v[si:ei+1])
        c1 = _max(si+1, ei)
        c2 = _max(si, ei-1)
        mem[key] = max(V-c1,V-c2)
        return mem[key]
    result = _max(0,len(v)-1)
    return result
