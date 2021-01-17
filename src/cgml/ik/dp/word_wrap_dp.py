#
# Complete the 'solveBalancedLineBreaks' function below.
#
# The function accepts STRING ARRAY and INTEGER as parameter.
# Return LONG.
#

def solveBalancedLineBreaks(words, limit):
    wc = [len(w) for w in words]
    if sum(wc) + len(wc) - 1 <= limit:
        return 0
    N = len(words)
    dp = [float('inf')]*N
    for idx in range(N):
        k = idx
        csum = wc[k]
        while csum <= limit:
            dp[idx]=min(dp[idx], (limit-csum)**3 + (dp[k-1] if k >=1 else 0) )
            k -= 1
            if k < 0:
                break
            csum += 1 + wc[k]
    k = N-1
    for idx in range(N-1, -1, -1):
        last_row = sum(wc[idx:]) + N-1-idx
        if last_row > limit:
            break
        k = idx
    return min(dp[k-1:])
