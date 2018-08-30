'''
Most significant digit first (MSD) string sort

Idea:
- Sort by first character and partition array into R pieces
- Recursively use same method on each piece
'''

def mds_ord(s,depth):
    result = 0 if len(s) <= depth else ord(s[depth])+1
    return result

def mds_radix_sort(ls):
    aux = [None]*len(ls)
    _mds_radix_helper(ls,aux,0,len(ls)-1,0)
    return ls

def _mds_radix_helper(ls, aux, lo, hi, d):
    if hi <= lo: return
    R = 256
    counts = [0]*(R+2)
    for i in range(lo, hi+1):
        counts[mds_ord(ls[i],d)+1] += 1

    for r in range(0,R+1):
        counts[r+1] += counts[r]

    for i in range(lo, hi+1):
        aux[ counts[ mds_ord(ls[i], d)] ] = ls[i]
        counts[mds_ord(ls[i], d)] += 1

    for i in range(lo, hi+1):
        ls[i] = aux[i-lo]

    # Sort pieces recursively
    for r in range(R):
        _mds_radix_helper(ls, aux, lo + counts[r], lo + counts[r+1]-1, d+1)


print(mds_radix_sort(["bnm","ask","asf","bdm","bde","yte","yaa","arv","vfr","dfs"]))