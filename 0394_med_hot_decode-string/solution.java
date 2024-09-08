import java.util.Stack;

class Solution {
    public String decodeString(String s) {
        Stack<Character> stack = new Stack<>();

        for (char c : s.toCharArray()) {
            if (c != ']') {
                stack.push(c);
            } else {
                // pop and decode
                StringBuilder token = new StringBuilder();
                while (stack.peek() != '[') {
                    token.insert(0, stack.pop());
                }
                stack.pop();  // remove '['

                StringBuilder numStr = new StringBuilder();
                while (!stack.isEmpty() && Character.isDigit(stack.peek())) {
                    numStr.insert(0, stack.pop());
                }

                int repeatCount = Integer.parseInt(numStr.toString());
                String repeatedToken = token.toString().repeat(repeatCount);
                
                for (char ch : repeatedToken.toCharArray()) {
                    stack.push(ch);
                }
            }
        }

        StringBuilder result = new StringBuilder();
        for (char ch : stack) {
            result.append(ch);
        }

        return result.toString();
    }
}