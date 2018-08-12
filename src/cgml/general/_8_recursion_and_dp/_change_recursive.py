class Profiler:
    recursive_call_counter = 0


def change_recursive(target,denoms):
    if target == 0: return []
    optimal_change = None
    for d in denoms:
        if target-d < 0: continue
        change = change_recursive(target-d,denoms)
        if optimal_change is None or len(change) < len(optimal_change): optimal_change = change + [d]
    Profiler.recursive_call_counter += 1
    return optimal_change

assert change_recursive(40,[25,10,5,1]) == [25,10,5]
assert Profiler.recursive_call_counter == 252592
assert change_recursive(40,[50,25,20,10,5,1]) == [20,20]
assert Profiler.recursive_call_counter == 510263
assert change_recursive(53,[50,25,20,10,5,1]) == [50,1,1,1]
assert Profiler.recursive_call_counter == 14463768