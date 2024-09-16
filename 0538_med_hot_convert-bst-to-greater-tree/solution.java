import java.util.ArrayList;
import java.util.List;

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
    public TreeNode convertBST(TreeNode root) {
        List<TreeNode> nodes = inorder(root);

        int size = nodes.size();

        for(int i = size - 1; i > 0; i--) {
            nodes.get(i-1).val += nodes.get(i).val;
        }

        return root;
    }

    private List<TreeNode> inorder(TreeNode root) {
        if(root == null) {
            return new ArrayList<>();
        }
        List<TreeNode> result = new ArrayList<>();

        result.addAll(inorder(root.left));
        result.add(root);
        result.addAll(inorder(root.right));

        return result;
    }

}