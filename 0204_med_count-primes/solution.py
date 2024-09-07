class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        
        marks = [1] * n
        
        marks[0] = marks[1] = 0
        
        for i in range(2, int(n ** 0.5) + 1):
            if marks[i]:
                marks[i*i:n:i] = [0] * len(marks[i*i:n:i])
                
        return sum(marks) 