# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):

from collections import deque

def read4(buf):
    pass


class Solution(object):
    def __init__(self):
        self.buf4 = [''] * 4
        self.start = 0
        self.end = 0

    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        idx = 0
        while self.start < self.end and idx < n:
            buf[idx] = self.buf4[self.start]
            self.start += 1
            idx += 1

        if self.start == self.end:
            self.start, self.end = 0, 0

        while idx < n:
            self.end = read4(self.buf4)

            if self.end == 0:
                break

            i = 0
            while i < min(self.end, n - idx):
                buf[idx + i] = self.buf4[i]
                i += 1

            self.start = i
            idx += i

        return idx

class SolutionIncorrect(object):
    q = deque([])  # None

    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        # if self.q is None: 
        #     self.q = deque([])

        while len(self.q) < n:
            res = read4(buf)
            print(res)
            for r in list(res): self.q.append(r)
            if res is None or res == "": break

        result = []
        while len(result) < n and len(self.q) > 0: result += self.q.popleft()

        return 