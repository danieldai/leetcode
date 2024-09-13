import java.util.Deque;
import java.util.LinkedList;

class Solution {
    public int evalRPN(String[] tokens) {
        Deque<Integer> stack = new LinkedList<>();

        for(String t : tokens) {
            if("+".equals(t)) {
                stack.push(stack.pop() + stack.pop());
            } else if ("-".equals(t)) {
                stack.push(-stack.pop() + stack.pop());
            } else if ("*".equals(t)) {
                stack.push(stack.pop() * stack.pop());
            } else if ("/".equals(t)) {
                int n2 = stack.pop();
                int n1 = stack.pop();
                stack.push(n1 / n2);
            } else {
                stack.push(Integer.valueOf(t));
            }
        }

        return stack.pop();

    }
}