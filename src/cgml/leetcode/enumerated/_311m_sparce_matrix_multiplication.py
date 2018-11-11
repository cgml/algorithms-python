import itertools
from collections import defaultdict

class Solution(object):
    def multiply(self, A, B):
        if not A or not B or not A[0] or not B[0]: return [[]]
        R, C = len(A), len(B[0])
        A, B, PROD = self._sparse(A), self._sparse(B, transposed=True), defaultdict(dict)
        for idx, idy in itertools.product(A, B):
            PROD[idx][idy] = sum([A[idx][eidx] * B[idy][eidx] for eidx in set(A[idx]) & set(B[idy])])

        result = [[PROD[ridx].get(cidx, 0) for cidx in range(C)] for ridx in range(R)]
        return result

    def _sparse(self, x, transposed=False):
        X = defaultdict(dict)
        for idx in range(len(x)):
            for idy in range(len(x[0])):
                if x[idx][idy] != 0:
                    if not transposed:
                        X[idx][idy] = x[idx][idy]
                    else:
                        X[idy][idx] = x[idx][idy]
        return X


print(Solution().multiply([[1,0,0],[-1,0,3]],[[7,0,0],[0,0,0],[0,0,1]]))
