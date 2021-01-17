def largest_sub_square_matrix(R, C, mat):
    dp = [[0]*(C+1) for _ in range(R+1)]
    for r in range(1,R+1):
        for c in range(1,C+1):
            dp[r][c] = (dp[r][c-1]+1) if mat[r-1][c-1] == 1 else 0
    maxs = 0
    for c in range(1,C+1):
        s=[(0,0)] #h, start
        for r in range(1,R+1):
            start = r # i
            while len(s)>0 and dp[r][c]<=s[-1][0]:
                _, start = s.pop()
            s.append((dp[r][c], start))
            maxs=max(maxs,min(dp[r][c], r-start+1))
    return maxs