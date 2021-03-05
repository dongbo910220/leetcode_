'''
https://leetcode.com/problems/sudoku-solver/submissions/
'''

class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        self.board = board
        self.solve()

    def findUnassigned(self):
        for row in range(9):
            for col in range(9):
                if self.board[row][col] == ".":
                    return row, col
        return -1, -1

    def solve(self):
        row, col = self.findUnassigned()

        if row == -1 and col == -1:
            return True
        for num in "123456789":
            if self.isSafe(row, col, num):
                self.board[row][col] = num
                if self.solve():
                    return True
                self.board[row][col] = '.'
        return False

    def isSafe(self, row, col, ch):
        boxrow = row // 3 * 3;
        boxcol = col // 3 * 3;
        if self.checkrow(row, ch) and self.checkcol(col, ch) and self.checkbox(boxrow, boxcol, ch):
            return True
        return False

    def checkrow(self, row, ch):
        for col in range(9):
            if self.board[row][col] == ch:
                return False
        return True

    def checkcol(self, col, ch):
        for row in range(9):
            if self.board[row][col] == ch:
                return False
        return True

    def checkbox(self, boxrow, boxcol, ch):
        for row in range(boxrow, boxrow + 3):
            for col in range(boxcol, boxcol + 3):
                if self.board[row][col] == ch:
                    return False
        return True

'''
Success
Details 
Runtime: 1008 ms, faster than 16.20% of Python online submissions for Sudoku Solver.
Memory Usage: 12.7 MB, less than 96.23% of Python online submissions for Sudoku Solver.'''