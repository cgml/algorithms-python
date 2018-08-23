import math

class Solution():
    def helper(self, n, mem, snum):
        if n<1: return []
        result = set()
        for i in range(snum, int(math.sqrt(n))+1):
            if n % i == 0:
                result.add((i, int(n/i)))
                for r in self.helper(int(n/i), mem, i): result.add(tuple(sorted([i]+[k for k in r])))
        mem[n]=result
        return result

    def factorize(self, n):
        mem = [0]*(n+1)
        result = self.helper(n, mem, 2)
        return [[k for k in r] for r in result]

print(Solution().factorize(1))
print(Solution().factorize(2))
print(Solution().factorize(5))
print(Solution().factorize(20))
print(Solution().factorize(2000))
print(Solution().factorize(2040))
print(len(Solution().factorize(1000000)), Solution().factorize(1000000))
print(len(Solution().factorize(10000000)), Solution().factorize(10000000))
print(len(Solution().factorize(10**8)))