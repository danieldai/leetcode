import java.util.Deque;
import java.util.LinkedList;

class Solution {
    public String removeDuplicates(String s) {
        Deque<Character> stack = new LinkedList<>();

        for (char c : s.toCharArray()) {
            if (!stack.isEmpty() && stack.peek() == c) {
                stack.pop();
            } else {
                stack.push(c);
            }
        }
        
        String result = "";
        while (!stack.isEmpty()) {
            result = stack.pop() + result;
        }

        return result;
    }
}