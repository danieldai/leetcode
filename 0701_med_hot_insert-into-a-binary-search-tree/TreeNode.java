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
    public TreeNode insertIntoBST(TreeNode root, int val) {
        TreeNode newNode = new TreeNode(val);

        if (root == null) {
            return newNode;
        }

        TreeNode ptr = root;
        
        while (true) {
            if (val < ptr.val) {
                if (ptr.left == null) {
                    ptr.left = newNode;
                    break;
                } else {
                    ptr = ptr.left;
                }
            } else {
                if (ptr.right == null) {
                    ptr.right = newNode;
                    break;
                } else {
                    ptr = ptr.right;
                }
            }
        }

        return root;
    }
}


class Solution2 {
    public TreeNode insertIntoBST(TreeNode root, int val) {
        if (root == null) {
            return new TreeNode(val);
        }

        if(val < root.val) {
            root.left = insertIntoBST(root.left, val);
        } else {
            root.right = insertIntoBST(root.right, val);
        }

        return root;
    }
}