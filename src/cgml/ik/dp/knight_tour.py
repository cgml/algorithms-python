def numPhoneNumbers(startdigit, phonenumberlength):
    dp = [[v for v in range(10)] for idx in range(phonenumberlength)]
    dp[0] = [1] * 10
    numpad = {
        0: [4, 6],
        1: [6, 8],
        2: [7, 9],
        3: [4, 8],
        4: [3, 9, 0],
        5: [],
        6: [0, 1, 7],
        7: [2, 6],
        8: [1, 3],
        9: [2, 4]
    }
    for idx in range(1, phonenumberlength):
        for c in range(10):
            nums = numpad[c]
            dp[idx][c] = sum([dp[idx - 1][v] for v in nums])
    return dp[-1][startdigit]
