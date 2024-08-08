class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        
        if len(strs) == 1:
            return strs[0]

        prefix = ""

        while True:
            if len(prefix) >= len(strs[0]):
                return prefix

            prefix = strs[0][:len(prefix)+1]
            for s in strs[1:]:
                if not s.startswith(prefix):
                    return prefix[:-1]