import java.util.ArrayList;
import java.util.List;
import java.util.Deque;
import java.util.LinkedList;

/**
 * Definition for a binary tree node.
 */

 class TreeNode {
     int val;
     TreeNode left;
     TreeNode right;
     TreeNode() {}
     TreeNode(int val) { this.val = val; }
     TreeNode(int val, TreeNode left, TreeNode right) {
         this.val = val;
         this.left = left;
         this.right = right;
     }
 }

class Solution {
    public List<Integer> postorderTraversal2(TreeNode root) {
        List<Integer> result = new ArrayList<>();
        Deque<TreeNode> stack = new LinkedList<>();

        TreeNode prevAccess = null;
        while(root != null || !stack.isEmpty()) {
            while(root != null) {
                stack.push(root);
                root=root.left;
            }

            root=stack.pop();
            if(root.right == null || root.right == prevAccess) {
                result.add(root.val);
                prevAccess = root;
                root = null;
            } else {
                stack.push(root);
                root=root.right;
            }
        }
        return result;
    }

    public List<Integer> postorderTraversal(TreeNode root) {
        List<Integer> result = new ArrayList<>();

        if(root != null) {
            result.addAll(postorderTraversal(root.left));
            result.addAll(postorderTraversal(root.right));
            result.add(root.val);
        }
        
        return result;
    }
}