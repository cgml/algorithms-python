def minMultiplicationCost(s):
    S = list(zip(s, s[1:]))
    N = len(S)
    dp = [[float('inf')] * N for _ in range(N)]
    for idx in range(N):
        dp[idx][idx] = 0
    for idd in range(1, N):
        idr = 0
        idc = idd
        while idc < N:
            for k in range(idr, idc):
                cc = dp[idr][k] + dp[k + 1][idc] + S[idr][0] * S[k + 1][0] * S[idc][1]
                dp[idr][idc] = min(dp[idr][idc], cc)
            idc += 1
            idr += 1
    return dp[0][-1]