class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(haystack)
        m = len(needle)

        if m == 0:
            return 0
        
        nextp = [0] * m

        j = 0
        print(list(needle))
        for i in range(1, m):
            if j > 0 and needle[i] != needle[j]:
                j = nextp[j - 1]

            if needle[i] == needle[j]:
                j += 1

            nextp[i] = j
            print([str(n) for n in nextp])
        
        j = 0
        for i in range(n):
            if j > 0 and haystack[i] != needle[j]:
                j = nextp[j - 1]

            if haystack[i] == needle[j]:
                j += 1

            if j == m:
                return i - m + 1
            
        return -1





class Solution2:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i+len(needle)] == needle:
                return i
        
        return -1
        

if __name__ == '__main__':
    Solution().strStr("sadbutsad", "abcddabcx")
