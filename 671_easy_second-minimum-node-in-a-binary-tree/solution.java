// Definition for a binary tree node.
class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    
    TreeNode() {}
    
    TreeNode(int val) {
        this.val = val;
    }
    
    TreeNode(int val, TreeNode left, TreeNode right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

class Solution {
    private long ans;

    public Solution() {
        this.ans = Long.MAX_VALUE;
    }

    public int findSecondMinimumValue(TreeNode root) {
        find(root, root);

        if (ans == Long.MAX_VALUE) {
            return -1;
        } else {
            return (int) ans;
        }
    }

    private void find(TreeNode node, TreeNode root) {
        if (node == null) {
            return;
        }

        if (node.val != root.val) {
            ans = Math.min(ans, node.val);
            return;
        } else {
            find(node.left, root);
            find(node.right, root);
        }
    }
}
