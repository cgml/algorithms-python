def lcs(a, b):
    A, B = len(a), len(b)
    dp=[[0]*(B+1) for _ in range(A+1)]
    for idr in range(1,A+1):
        for idc in range(1,B+1):
            options = [dp[idr-1][idc], dp[idr][idc-1], dp[idr-1][idc-1]+ (1 if a[idr-1] == b[idc-1] else 0)]
            dp[idr][idc]=max(options)
    idr = A
    idc = B
    result = ""
    while idr > 0 and idc > 0:
        if a[idr-1] == b[idc-1] and (dp[idr-1][idc-1] + 1) > dp[idr-1][idc] and (dp[idr-1][idc-1] + 1) > dp[idr][idc-1]:
            result = a[idr-1]+result
            idr -=1
            idc -=1
        elif dp[idr-1][idc] > dp[idr][idc-1]:
            idr -= 1
        else:
            idc -= 1
    return result if result else "-1"