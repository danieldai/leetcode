from typing import List


class Solution:
    chars = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        if len(digits) == 1:
            return list(Solution.chars[digits[0]])
                
        res = []
        for a in Solution.chars[digits[0]]:
            for s in self.letterCombinations(digits[1:]):
                res.append(a+s)
        return res
    

class Solution2:
    chars = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        if len(digits) == 1:
            return list(Solution.chars[digits[0]])
                
        res = [letter for letter in Solution.chars[digits[0]]]

        for digit in digits[1:]:
            res = [a + b for a in res for b in Solution.chars[digit]]

        return res
    

class Solution3:
    def __init__(self):
        self.letterMap = [
            "",     # 0
            "",     # 1
            "abc",  # 2
            "def",  # 3
            "ghi",  # 4
            "jkl",  # 5
            "mno",  # 6
            "pqrs", # 7
            "tuv",  # 8
            "wxyz"  # 9
        ]
        self.result = []
    
    def getCombinations(self, digits, index, s):
        if index == len(digits):
            self.result.append(s)
            return
        
        digit = int(digits[index])
        letters = self.letterMap[digit]
        for letter in letters:
            self.getCombinations(digits, index + 1, s + letter)
    
    def letterCombinations(self, digits):
        if len(digits) == 0:
            return self.result
        self.getCombinations(digits, 0, "")
        return self.result