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
    public TreeNode buildTree(int[] inorder, int[] postorder) {
        if(inorder.length == 0 && postorder.length == 0) {
            return null;
        }
        if(inorder.length == 1 && postorder.length == 1) {
            return new TreeNode(inorder[0]);
        }

        int size = inorder.length;

        TreeNode node = new TreeNode(postorder[size-1]);

        // int leftCount = Arrays.index

        return node;
    }
}