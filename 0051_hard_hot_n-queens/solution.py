from typing import List


class Solution:
    def __init__(self) -> None:
        self.result = []

    def solveNQueens(self, n: int) -> List[List[str]]:
        self.backtracking(n, 0, [["."] * n] * n)
        return self.result

    def backtracking(self, n: int, row: int, chessboard: List[str]):
        if row == n:
            self.result.append([''.join(row) for row in chessboard])
            return
        
        for col in range(n):
            if self.is_valid(row, col, chessboard, n):
                chessboard[row][col] = "Q"
                self.backtracking(n, row + 1, chessboard)
                chessboard[row][col] = "."


    def is_valid(self, row: int, col: int, chessboard: List[str], n: int):
        # 检查同一列
        for i in range(row):
            if chessboard[i][col] == "Q":
                return False
            
        # 检查 45度角是否有皇后
        i = row - 1
        j = col - 1
        while i >= 0 and j >= 0:
            if chessboard[i][j] == "Q":
                return False
            i -= 1
            j -= 1

        #  检查 135度角是否有皇后
        i = row - 1
        j = col + 1
        while i >= 0 and j < n:
            if chessboard[i][j] == "Q":
                return False
            i -= 1
            j += 1

        return True
            
        