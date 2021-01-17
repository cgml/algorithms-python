def countWaysToClimb(steps, n):
    dp = [0]*(n+1)
    dp[0] = 1
    for idx in range(1,n+1):
        s = 0
        for step in sorted(steps):
            if step > idx:
                break
            s += dp[idx-step]
        dp[idx] = s
    return dp[-1]