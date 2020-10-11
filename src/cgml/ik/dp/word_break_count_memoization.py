#
# Complete the 'wordBreakCount' function below.
#
# The function accepts STRING_ARRAY dictionary as parameter
# and the original STRING txt on which segmentation is to be
# performed.
# The function returns the count of all possible segmentation
#
import resource, sys
resource.setrlimit(resource.RLIMIT_STACK, (2**29,-1))
sys.setrecursionlimit(10**6)

def wordBreakCount(dictionary, txt):
    words = set(dictionary)
    mem = {}

    def _helper(txt, idx):
        if idx == len(txt):
            return 1
        if mem.get(idx) is not None:
            return mem[idx]
        result = 0
        for idy in range(idx, len(txt)+1):
            if txt[idx:idy] in words:
                result += _helper(txt, idy)
        mem[idx]=result % 1000000007
        return result
    result = _helper(txt, 0)
    return result % 1000000007
