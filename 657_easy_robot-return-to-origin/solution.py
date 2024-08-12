class Solution:
    def judgeCircle(self, moves: str) -> bool:
        R = L = U = D = 0

        for m in moves:
            if m == "R":
                R += 1
            if m == "L":
                L += 1
            if m == 'U':
                U += 1
            if m == 'D':
                D += 1
        
        return R == L and U == D
        