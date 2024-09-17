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
    public TreeNode trimBST(TreeNode root, int low, int high) {
        if (root == null) {
            return null;
        }

        // If the current node's value is within the range [low, high]
        if (low <= root.val && root.val <= high) {
            root.left = trimBST(root.left, low, high);
            root.right = trimBST(root.right, low, high);
            return root;
        } 

        // If the current node's value is less than the low boundary
        if (root.val < low) {
            return trimBST(root.right, low, high);
        } 

        // If the current node's value is greater than the high boundary
        return trimBST(root.left, low, high);  
    }
}