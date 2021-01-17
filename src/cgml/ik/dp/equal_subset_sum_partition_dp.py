def equalSubSetSumPartition(s):
    N = len(s)
    if N < 2 or sum(s) % 2 != 0:
        return []
    dp = [set() for idx in range(N)]
    dp[0].add(s[0])
    for idx in range(1,N):
        dp[idx].add(s[idx])
        for v in dp[idx-1]:
            dp[idx].add(v)
            dp[idx].add(v+s[idx])
    t = sum(s)//2
    if t not in dp[-1]:
        return []
    result = [False]*N
    cnt = 0
    for idx in range(N-1, -1, -1):
        if idx > 0:
            if t in dp[idx] and t not in dp[idx-1]:
                result[idx] = True
                t-=s[idx]
                cnt +=1
                if t == 0:
                    break
        else:
            cnt += 1
            result[0] = True

    if cnt == N:
        return []
    return result