from typing import List


class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        results = []

        if '+' not in expression and '-' not in expression and '*' not in expression:
            results.append(int(expression))
        
        else:
            for i in range(len(expression)):
                if expression[i] in '+-*':
                    left = self.diffWaysToCompute(expression[:i])
                    right = self.diffWaysToCompute(expression[i+1:])
                    if expression[i] == '+':
                        results.extend([i+j for i in left for j in right])
                    if expression[i] == '-':
                        results.extend([i-j for i in left for j in right])
                    if expression[i] == '*':
                        results.extend([i*j for i in left for j in right])
        return results