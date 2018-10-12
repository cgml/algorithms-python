import numpy as np
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2: return 0
        primes = np.ones(int(n / 2), dtype=np.bool)
        for i in range(3, int(n ** 0.5) + 1, 2):
            if primes[int(i / 2)]: primes[int(i * i / 2)::i] = False
        return int(primes.sum())


class SolutionConventional(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        primes = []
        for idx in range(2, n):
            prime = True
            idx_sqrt = int(idx**0.5)
            for p in primes:
                if p > idx_sqrt: break
                if idx % p == 0:
                    prime = False
                    break
            if prime: primes.append(idx)
        return len(primes)

# function is_prime(n)
#     if n ≤ 1
#        return false
#     else if n ≤ 3
#        return true
#     else if n mod 2 = 0 or n mod 3 = 0
#        return false
#     let i ← 5
#     while i * i ≤ n
#        if n mod i = 0 or n mod (i + 2) = 0
#            return false
#        i ← i + 6
#     return true


print(Solution().countPrimes(int(10**5)))