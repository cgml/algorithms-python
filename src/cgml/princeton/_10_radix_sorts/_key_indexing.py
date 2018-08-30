'''
Sort a integers, where integers are between 0 and R-1

Time Complexity: O(N+R)
Space Complexity: O(N+R)

Stable: Yes
'''

def key_indexing(a,R):
    N = len(a)
    counts = [0]*(R+1)
    aux = [None]*N
    # Calculate counts
    for idx in range(N): counts[a[idx]+1]+=1

    # Calculate cumulative sums
    for idx in range(R): counts[idx+1]+=counts[idx]

    # Move items
    for idx in range(N):
        aux[counts[a[idx]]]=a[idx]
        counts[a[idx]]+=1

    # Move items back
    for idx in range(N): a[idx]=aux[idx]

    return a


print(key_indexing([1,2,3,1,2,3,4,1,2,3,4,5,6,1,2,3,4,2,2,2,6,4,4,3,4,5],R=7))