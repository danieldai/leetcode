from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.backtracking(board)

    def backtracking(self, board: List[List[str]]):
        n = len(board)
        for i in range(n):
            for j in range(n):
                if board[i][j] == ".":
                    for val in range(1, 10):
                        val = str(val)
                        if self.is_valid(i, j, val, board):
                            board[i][j] = val
                            if self.backtracking(board):
                                return True
                            board[i][j] = "."
                    return False
            
        return True

    
    def is_valid(self, row: int, col: int, val: str, board: List[List[str]]) -> bool:
        # 判断行里是否重复
        for i in range(9):
            if board[row][i] == val:
                return False

        # 判断列里是否重复
        for i in range(9):
            if board[i][col] == val:
                return False

        # 判断9方格里是否重复
        rowStart = row // 3 * 3
        colStart = col // 3 * 3
        for i in range(rowStart, rowStart + 3):
            for j in range(colStart, colStart + 3):
                if board[i][j] == val:
                    return False

        return True


if __name__ == "__main__":
    board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
    Solution().solveSudoku(board)
    print(board)