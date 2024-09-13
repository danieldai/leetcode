class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        n = len(s)
        result = ""

        for i in range(0, n, 2 * k):
            
            result += s[i:min(i + k, n)][::-1]
            if n > i + k:
                result += s[i + k:min(i + 2 * k, n)]
        
        return result
        

        