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
    int maxDepth = -1;
    int result = 0;
    public int findBottomLeftValue(TreeNode root) {
        if (root == null) {
            return 0;
        }
        findLeftValue(root, 1);
        return result;
    }

    private void findLeftValue(TreeNode node, int depth) {
        if(node == null) {
            return;
        }
        if(node.left == null && node.right == null && depth > maxDepth) {
            maxDepth = depth;
            result = node.val;
        }
        findLeftValue(node.left, depth+1);
        findLeftValue(node.right, depth+1);
    }
}