class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        words = set(wordDict)
        results = []

        L = min(10, len(s))
        # print(s)
        for i in range(1,L+1):
            if s[:i] in words:
                # print("s: %s, s[:i] %s " % (s, s[:i]))
                if len(s[:i]) == len(s):
                  results.append(s[:i])
                  break
                result = self.wordBreak(s[i:], wordDict)
                
                results.extend([ s[:i] + ' ' + r for r in result ])
                # print("s: %s, s[:i]: %s, result: %s, results: %s" % (s, s[:i], result, results))
        
        return results