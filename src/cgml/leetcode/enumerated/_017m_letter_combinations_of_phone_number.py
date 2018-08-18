import itertools


class Solution():
    def letterCombinations(self, digits):
        if not digits: return []
        solution = []
        curs = ['']*len(digits)
        combinations = [list(k) for k in [' ',' ', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']]
        self.helper(solution, curs, combinations, digits, 0)
        return solution

    def helper(self, solution, curs, combinations, digits, idx):
        if idx>=len(digits): solution.append(''.join(curs))
        else:
            for letter in combinations[ord(digits[idx]) - ord('0')]:
                curs[idx]=letter.strip()
                self.helper(solution, curs, combinations, digits, idx+1)

class SolutionCheating():
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []

        digit_map = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }

        s = []
        for digit in digits:
            if digit in digit_map: s.append(list(digit_map[digit]))

        result = []
        for t in list(itertools.product(*s)):
            result.append(''.join(t))

        return result

print(Solution().letterCombinations("123456"))