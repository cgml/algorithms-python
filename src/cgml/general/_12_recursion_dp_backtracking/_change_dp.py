from cgml.general._12_recursion_dp_backtracking.utils import *

def change_dp_count(target,denoms):
    minnums = [0]*(target+1)
    for m in range(1,target+1):
        minnums[m]=target*target # =~ infinity
        for coin in denoms:
            if m >= coin:
                numcoins = minnums[m-coin] + 1
                if numcoins < minnums[m]: minnums[m]=numcoins
                Profiler.increment()
    return minnums[target]


def change_dp(target,denoms):
    minnums = [[]]*(target+1)
    for m in range(1,target+1):
        minnums[m]=[1]*target # =~ infinity. assume we have coin with denom 1
        for coin in denoms:
            if m >= coin:
                numcoins = minnums[m-coin] + [coin]
                if len(numcoins) < len(minnums[m]): minnums[m]=numcoins
                Profiler.increment()
    return minnums[target]


Profiler.reset()

assert change_dp_count(53,[50,25,20,10,5,1]) == 4
assert Profiler.popcounter() == 213

assert change_dp(53,[50,25,20,10,5,1]) == [1,1,1,50]
assert Profiler.popcounter() == 213

assert change_dp(97,[50,25,20,10,5,1]) == [1, 1, 20, 25, 50]
assert Profiler.popcounter() == 477