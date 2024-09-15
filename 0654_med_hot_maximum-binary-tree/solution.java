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
    public TreeNode constructMaximumBinaryTree(int[] nums) {
        if (nums.length == 0) {
            return null;
        }

        if (nums.length == 1) {
            return new TreeNode(nums[0]);
        }

        return constructMaximumBinaryTree(nums, 0, nums.length);
    }

    private TreeNode constructMaximumBinaryTree(int[] nums, int left, int right) {
        if (left == right) {
            return null;
        }

        int maxValue = nums[left];
        int maxIndex = left;
        for (int i = left; i < right; i++) {
            if (nums[i] > maxValue) {
                maxValue = nums[i];
                maxIndex = i;
            }
        }
        
        TreeNode node = new TreeNode(maxValue);
        node.left = constructMaximumBinaryTree(nums, left, maxIndex);
        node.right = constructMaximumBinaryTree(nums, maxIndex+1, right);

        return node;
    } 
}