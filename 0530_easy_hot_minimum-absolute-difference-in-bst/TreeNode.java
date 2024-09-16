import java.util.*;
/**
 * Definition for a binary tree node.
 */

public class TreeNode {
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


// 使用递归的方法中序序遍历
class Solution {
    int minDiff = Integer.MAX_VALUE;
    TreeNode prev = null;

    public int getMinimumDifference(TreeNode root) {
        inorder(root);
        return minDiff;
    }

    private void inorder(TreeNode root) {
        if(root == null) {
            return;
        }

        inorder(root.left);
        if (prev != null) {
            minDiff = Math.min(minDiff, root.val - prev.val);
        }
        prev = root;
        inorder(root.right);
    }
}


// 使用迭代的方法中序序遍历
class Solution2 {
    int minDiff = Integer.MAX_VALUE;
    TreeNode prev = null;

    public int getMinimumDifference(TreeNode root) {
        inorder(root);
        return minDiff;
    }

    private void inorder(TreeNode root) {
        if(root == null) {
            return;
        }

        Deque<TreeNode> stack = new LinkedList<>();

        TreeNode cur = root;

        while (cur != null || !stack.isEmpty()) {
            while (cur != null) {
                stack.push(cur);
                cur = cur.left;
            }

            cur = stack.pop();

            if(prev != null) {
                minDiff = Math.min(minDiff, cur.val - prev.val);
            }
            prev = cur;

            cur = cur.right;
        }
        
    }
}

// 使用迭代的方法中序序遍历2
class Solution3 {
    int minDiff = Integer.MAX_VALUE;
    TreeNode prev = null;

    public int getMinimumDifference(TreeNode root) {
        inorder(root);
        return minDiff;
    }

    private void inorder(TreeNode root) {
        if(root == null) {
            return;
        }

        Deque<TreeNode> stack = new LinkedList<>();

        TreeNode cur = root;

        while (cur != null || !stack.isEmpty()) {
            if (cur != null) {
                stack.push(cur);
                cur = cur.left;
            } else {
                cur = stack.pop();

                if(prev != null) {
                    minDiff = Math.min(minDiff, cur.val - prev.val);
                }
                prev = cur;

                cur = cur.right;
            }
        }
    }
}