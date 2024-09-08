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

    public boolean isSymmetric2(TreeNode root) {
        Deque<TreeNode> queue = new LinkedList<>();

        queue.push(root.left);
        queue.push(root.right);

        while (!queue.isEmpty()) {
            TreeNode a = queue.pop();
            TreeNode b = queue.pop();

            if(a == null && b == null) {
                continue;
            }

            if(a == null || b == null) {
                return false;
            }

            if(a.val != b.val) {
                return false;
            }

            queue.push(a.left);
            queue.push(b.right);
            queue.push(a.right);
            queue.push(b.left);

        }

        return true;
    }

    public boolean isSymmetric(TreeNode root) {
        if (root == null) {
            return true;
        }

        return isSymmetric(root.left, root.right);
    }

    private boolean isSymmetric(TreeNode left, TreeNode right) {
        if (left == null && right == null) {
            return true;
        }

        if (left == null || right == null) {
            return false;
        }

        return (left.val == right.val && 
             isSymmetric(left.left, right.right) &&
             isSymmetric(left.right, right.left));
    }
}