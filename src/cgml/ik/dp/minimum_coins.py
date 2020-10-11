def minimum_coins(coins, value):
    coinset, N = sorted(coins), value
    result = [float('inf')]*(N+1)
    result[0]=0
    for idx in range(1,N+1):
        for coin in coinset:
            if coin <= idx:
                result[idx]=min(result[idx], result[idx-coin]+1)
            else:
                break
    return result[N]