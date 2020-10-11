# Correct and optimal theoretically, but not optimal in practice
def equalSubSetSumPartition(s):
    mem = {}
    def _helper(target, i, e, idx):
        if target == 0 and idx <= len(s) and (i + e) > 1 and i < len(s) and e < len(s):
            return []
        if idx == len(s):
            return None
        if mem.get(str(target) + ":" + str(idx)) is not None:
            return mem[str(target) + ":" + str(idx)]
        result = None

        include_result = _helper(target=target - s[idx], i=i + 1, e=e, idx=idx + 1)
        if include_result is not None:
            result = [idx] + include_result
        else:
            exclude_result = _helper(target=target, i=i, e=e + 1, idx=idx + 1)
            if exclude_result is not None:
                result = exclude_result
        mem[str(target) + ":" + str(idx)] = result
        return result

    target = sum(s) / 2
    result = _helper(target=target, i=0, e=0, idx=0)
    if result is not None:
        result = set(result)
        return [v in result for v in range(len(s))]
    else:
        return []