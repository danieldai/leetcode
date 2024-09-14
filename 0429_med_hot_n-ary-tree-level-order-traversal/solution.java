/*
// Definition for a Node.
*/

import java.util.*;

class Node {
    public int val;
    public List<Node> children;

    public Node() {}

    public Node(int _val) {
        val = _val;
    }

    public Node(int _val, List<Node> _children) {
        val = _val;
        children = _children;
    }
};

class Solution {
    public List<List<Integer>> levelOrder(Node root) {
        if(root == null) {
            return new ArrayList<>();
        }

        List<List<Integer>> result = new ArrayList<>();

        Queue<Node> queue = new LinkedList<>();

        queue.offer(root);

        while (!queue.isEmpty()) {
            int size =  queue.size();
            List<Integer> levelResult = new ArrayList<>();
            while (size-- > 0) {
                Node node = queue.poll();
                levelResult.add(node.val);
                if(node.children != null) {
                    queue.addAll(node.children);
                }
            }
            result.add(levelResult);
        }

        return result;
    }
}