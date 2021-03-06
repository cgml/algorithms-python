class Solution:
    def solveSudoku(self, board):
        def isValid(board, x, y):
            for i in range(9):
                if i != x and board[i][y] == board[x][y]: return False
            for j in range(9):
                if j != y and board[x][j] == board[x][y]: return False
            i = 3 * (x / 3)
            while i < 3 * (x / 3 + 1):
                j = 3 * (y / 3)
                while j < 3 * (y / 3 + 1):
                    if (i != x or j != y) and board[i][j] == board[x][y]: return False
                    j += 1
                i += 1
            return True

        def solver(board):
            for i in range(len(board)):
                for j in range(len(board[0])):
                    if(board[i][j] == '.'):
                        for k in range(9):
                            board[i][j] = chr(ord('1') + k)
                            if isValid(board, i, j) and solver(board): return True
                            board[i][j] = '.'
                        return False
            return True

        solver(board)
board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
print(Solution().solveSudoku(board))