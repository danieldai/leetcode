from typing import List


class Solution:
    def __init__(self):
        self.w = 0
        self.h = 0
        
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board:
            return False
        
        if not word:
            return True
        
        self.h = len(board)
        self.w = len(board[0])
        
        for i in range(self.h):
            for j in range(self.w):
                if self.search(board, word, i, j, 0):
                    return True
        return False
    
    def search(self, board, word, i, j, d):
        
        if i < 0 or i == self.h or j < 0 or j == self.w or word[d] != board[i][j]:
            return False
        
        if d == len(word) - 1:
            return True
        
        char = board[i][j]
        
        board[i][j] = None
        
        found = (self.search(board, word, i+1, j, d+1) or 
                self.search(board, word, i-1, j, d+1) or
                self.search(board, word, i, j+1, d+1) or
                self.search(board, word, i, j-1, d+1))
                
        board[i][j] = char
        
        return found

        