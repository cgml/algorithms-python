def maxStolenValue(values):
    dp = [0]*len(values)
    dp[0]=values[0]
    for idx in range(1,len(values)):
        dp[idx]=max(values[idx] if idx == 1 else values[idx]+dp[idx-2], dp[idx-1])
    return dp[-1]
