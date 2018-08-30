'''
Least-Significant-digit-first string sort
- Stably sort dth character as a key using key indexed counting

Time Complexity: O(WN)
Space Complexity: O(N+R)
Stable: Yes
Operation on keys: character at (+ord)

Idea:
- Multiple paths from dth to 1st on characters on string gives fully sorted array of strings

Further:
- integers up to 64 bits can be broken into 4 characters of 16,
    which gives linear time O(4N) sorting time for Int64 arrays 

'''

def lsd_radix_string_sort(ls, W):
    R = 256
    N = len(ls)
    aux = [None]*N
    for d in range(W)[::-1]:
        counts = [0]*(R+1)
        # Calculating counts
        for i in range(N):
            counts[ord(ls[i][d])+1] += 1

        # Calculating cumulative sums
        for r in range(R): counts[r+1] += counts[r]

        # Copy items
        for i in range(N):
            aux[counts[ord(ls[i][d])]] = ls[i]
            counts[ord(ls[i][d])] += 1

        # Copy sorted items back
        ls[:] = aux[:]
    return ls

print(lsd_radix_string_sort(["bnm","ask","asf","bdm","bde","yte","yaa","arv","vfr","dfs"],3))