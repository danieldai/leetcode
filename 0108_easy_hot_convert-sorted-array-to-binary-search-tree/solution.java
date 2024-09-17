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
    public TreeNode sortedArrayToBST(int[] nums) {
        if (nums == null || nums.length == 0) {
            return null;
        }

        return sortedArrayToBST(nums, 0, nums.length);

    }

    private  TreeNode sortedArrayToBST(int[] nums, int left, int right) {
        if(left >= right) {
            return null;
        }

        if (right - left == 1) {
            return new TreeNode(nums[left]);
        }

        int middle = (right - left) / 2;

        TreeNode root = new TreeNode(nums[middle]);

        root.left = sortedArrayToBST(nums, left, middle);
        root.right = sortedArrayToBST(nums, middle+1, right);

        return root;
    }
}