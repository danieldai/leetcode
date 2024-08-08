class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = len(s)
        if length < 2:
            return length
        
        result = 0
        
        char_set = set()
        
        i = 0
        j = 0
        while i < length and j < length:
            if s[j] not in char_set:
                char_set.add(s[j])
                result = max(result, len(char_set))
                j += 1
            else:
                while s[i] != s[j]:
                    char_set.remove(s[i])
                    i += 1
                char_set.remove(s[i])
                i += 1
        return result