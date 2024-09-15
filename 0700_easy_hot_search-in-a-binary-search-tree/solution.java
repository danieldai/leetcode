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
    public TreeNode searchBST(TreeNode root, int val) {
        if (root == null) {
            return null;
        }

        TreeNode ptr = root;

        while(ptr != null) {
            if(val < ptr.val) {
                ptr = ptr.left;
            } else if (val > ptr.val) {
                ptr = ptr.right;
            } else if (val == ptr.val) {
                break;
            }

        }

        return ptr;
    }
}