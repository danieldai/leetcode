

'''
Example 1:

Input: s = "3[a]2[bc]"
Output: "aaabcbc"
Example 2:

Input: s = "3[a2[c]]"
Output: "accaccacc"
Example 3:

Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"
'''
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for c in s:
            if c != ']':
                stack.append(c)
            else:
                # pop and decode
                token = ""
                while stack[-1] != '[':
                    token = stack.pop() + token
                stack.pop()

                num_str = ""

                while stack[-1].isdigit():
                    num_str = stack.pop() + num_str
                stack.extend(token * int(num_str))
                
        return ''.join(stack)
