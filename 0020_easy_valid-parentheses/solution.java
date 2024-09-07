import java.util.Deque;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.Map;

class Solution {
    public boolean isValid(String s) {
        Map<Character, Integer> openings = new HashMap<>();
        openings.put('(', 1);
        openings.put('[', 2);
        openings.put('{', 3);
        
        Map<Character, Integer> closings = new HashMap<>();
        closings.put(')', 1);
        closings.put(']', 2);
        closings.put('}', 3);
        
        Deque<Character> stack = new LinkedList<>();
        
        for (char c : s.toCharArray()) {
            if (openings.containsKey(c)) {
                stack.push(c);
            } else {
                if (stack.isEmpty() || openings.get(stack.pop()) != closings.get(c)) {
                    return false;
                }
            }
        }
        
        return stack.isEmpty();
    }
}
