def maxWin(v):
    N = len(v)
    dp = [[None] * N for _ in range(N)]
    dpS = [[None] * N for _ in range(N)]
    for idx in range(N):
        dp[idx][idx] = v[idx]
        dpS[idx][idx] = v[idx]
    for idd in range(1, N):
        idr, idc = 0, idd
        while idc < N:
            dpS[idr][idc] = dpS[idr][idc - 1] + v[idc]
            dp[idr][idc] = dpS[idr][idc] - min(dp[idr][idc - 1], dp[idr + 1][idc])
            idr += 1
            idc += 1
    return dp[0][-1]
