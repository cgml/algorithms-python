# Not completed
def equalSubSetSumPartition(s):
    if sum(s) % 2 != 0:
        return []
    ps = [v for v in s if v >= 0]
    ns = [v for v in s if v < 0]
    left = min(s) if len(ns) == 0 else sum(ns)  # minus smallest
    right = max(s) if len(ps) == 0 else sum(ps)  # minus smallest
    offset = left
    totalrange = abs(right - left)
    R, C = len(s), totalrange + 1
    tbl = [[None] * (C) for _ in range(R)]
    for idr in range(R):
        for c in range(C):
            # e.g if range -3 to 20. offset is -3
            # for 0 column adjusted_sum will be 0 + (-3)
            # not used: adjusted_sum = c + offset

            # for s[idr] == -3 adjusted_sidr_value will be -3 - (-offset) = -3 -(-3) = 0
            adjusted_sidr_curr_value = s[idr] - offset
            # print('r={},c={},adj_cur_val={}'.format(idr,c,adjusted_sidr_curr_value))
            tbl[idr][c] = (adjusted_sidr_curr_value == c) or idr > 0 and (
                        tbl[idr - 1][c] or tbl[idr - 1][c - adjusted_sidr_curr_value])

    adjusted_target = sum(s) // 2 - offset
    curr_target = adjusted_target
    curr_idr = len(s) - 1
    if not tbl[curr_idr][curr_target]:
        return []
    s1 = []
    while curr_idr >= 0:
        adjusted_sidr_curr_value = s[curr_idr] - offset
        if tbl[curr_idr - 1][curr_target]:
            curr_idr -= 1
        elif tbl[curr_idr - 1][curr_target - adjusted_sidr_curr_value]:
            curr_target -= adjusted_sidr_curr_value
            s1.append(curr_idr)
            curr_idr -= 1
        else:
            # should never happen
            raise Exception('Error in dp table')

    s1 = set(s1)
    result = [idx in s1 for idx, v in enumerate(s)]
    return result