import numpy as np


class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not board or not board[0]: return False
        R, C = len(board), len(board[0])
        mem = [[0 for _ in range(C)] for _ in range(R)]  # np.zeros((R,C))
        for r in range(R):
            for c in range(C):
                if self._helper(board, word, r, c, 0, mem): return True
        return False

    def _helper(self, board, word, r, c, idx, mem):
        R, C = len(board), len(board[0])
        if r < 0 or c < 0 or r >= R or c >= C: return False
        if mem[r][c] != 0 or board[r][c] != word[idx]: return False
        if idx == len(word) - 1: return True
        mem[r][c] = 1
        for r2, c2 in [(r - 1, c), (r, c - 1), (r + 1, c), (r, c + 1)]:
            if self._helper(board, word, r2, c2, idx + 1, mem): return True
        mem[r][c] = 0
        return False
