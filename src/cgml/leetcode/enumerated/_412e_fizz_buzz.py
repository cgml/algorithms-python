class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        for idx in range(1,n+1):
            if idx % 3 == 0 and idx % 5 == 0: c = "FizzBuzz"
            elif idx % 3 == 0: c = "Fizz"
            elif idx % 5 == 0: c = "Buzz"
            else: c = str(idx)
            result.append(c)
        return result