from collections import deque

class SolutionBFS(object):
    def removeInvalidParentheses(self, s): #O(n^4)
        queue, ans, found, visited = deque([s]), [], False, set()
        while queue and not found:
            N = len(queue)
            for _ in range(N): #O(n)
                tmp = queue.popleft()

                if self.isValid(tmp):
                    ans.append(tmp)
                    found = True

                if not found:
                    for idx in range(len(tmp)): #O(n)
                        if tmp[idx] in ['(', ')']:
                            candidate = tmp[:idx] + tmp[idx+1:] #O(n)
                            if candidate not in visited:
                                queue.append(candidate)
                                visited.add(candidate)
            if found:
                break
        return ans

    def isValid(self, s): #O(n)
        cnt = 0
        for c in s:
            if c == '(': cnt += 1
            elif c == ')': cnt -= 1
            elif cnt < 0: return False
        return cnt == 0


class Solution(object):
    def _valid(self, s):
        counter = 0
        for c in s:
            if c == ")":
                counter -= 1
            elif c == "(":
                counter += 1
            if counter < 0: return False
        return counter == 0

    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        result = self.helper([s])
        return [k for k in result] if len(result) > 0 else [s.replace("(").replace(")")]

    def helper(self, candidates):
        result = set()
        for c in candidates:
            if self._valid(c): result.add(c)
        if len(result) > 0: return result

        newcandidates = set()
        for cs in candidates:
            for idx, c in enumerate(cs):
                if c in ['(', ')']: newcandidates.add(cs[:idx] + cs[idx + 1:])
        return self.helper(newcandidates)


'''
DFS or backtracking solution. It's 10X faster than optimized BFS.
    Limit max removal rmL and rmR for backtracking boundary. Otherwise it will exhaust all possible valid substrings, not shortest ones.
    Scan from left to right, avoiding invalid strs (on the fly) by checking num of open parenths.
    If it's '(', either use it, or remove it.
    If it's '(', either use it, or remove it.
    Otherwise just append it.
    Lastly set strings to the last decision point.

In each step, make sure:
    i does not exceed s.length().
    Max removal rmL rmR and num of open parens are non negative.
    De-duplicate by adding to a HashSet.
'''

class SolutionBacktrackingDFS:

    def removeInvalidParentheses(self, s):
        result = set()
        lb, rb = 0, 0
        for char in s:
            if char == '(': lb += 1
            elif char == ')':
                if lb > 0: lb -= 1
                else: rb += 1

        def rip(s, st, i, lb, rb, open_):
            if i == len(s) and lb == 0 and rb == 0 and open_ == 0:
                result.add(str(st))
                return

            if lb < 0 or rb < 0 or open_ < 0 or i == len(s): return

            if s[i] == '(':
                rip(s, st + s[i], i + 1, lb, rb, open_ + 1)
                rip(s, st, i + 1, lb - 1, rb, open_)

            elif s[i] == ')':
                rip(s, st + s[i], i + 1, lb, rb, open_ - 1)
                rip(s, st, i + 1, lb, rb - 1, open_)

            else:
                rip(s, st + s[i], i + 1, lb, rb, open_)

        rip(s, "", 0, lb, rb, 0)
        return list(result)

print(SolutionBacktrackingDFS().removeInvalidParentheses("(a)())((((()(())((("))
print(SolutionBFS().removeInvalidParentheses("(a)())"))