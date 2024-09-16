import java.util.*;
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
    int maxCount = 0;
    int count = 0;
    TreeNode prev = null;
    List<Integer> result = new ArrayList<>();

    public int[] findMode(TreeNode root) {
        searchBST(root);
        return result.stream().mapToInt(Integer::intValue).toArray();
    }

    private void searchBST(TreeNode root) {
        if (root == null) {
            return;
        }

        searchBST(root.left);

        if(prev == null) {
            count = 1;
        } else if(prev.val == root.val) {
            count++;
        } else {
            count = 1;
        }

        if(count == maxCount) {
            result.add(root.val);
        }

        if(count > maxCount) {
            maxCount = count;
            result.clear();
            result.add(root.val);
        }

        prev = root;

        searchBST(root.right);

    }
}