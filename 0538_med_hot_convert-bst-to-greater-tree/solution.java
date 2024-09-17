import java.util.ArrayList;
import java.util.Deque;
import java.util.LinkedList;
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

// 递归法，反中序遍历，右中左
class Solution2 {
    int addon = 0;

    public TreeNode convertBST(TreeNode root) {
        if (root == null) {
            return null;
        }

        inorder(root);

        return root;
    }

    private void inorder(TreeNode root) {
        if(root == null) {
            return;
        }

        inorder(root.right);

        root.val += addon;
        addon = root.val;

        inorder(root.left);
    }

}


class Solution3 {
    int addon = 0;

    public TreeNode convertBST(TreeNode root) {
        if (root == null) {
            return null;
        }

        inorder(root);

        return root;
    }

    private void inorder(TreeNode root) {
        if(root == null) {
            return;
        }

        Deque<TreeNode> stack = new LinkedList<>();
        TreeNode cur = root;

        while(cur != null || !stack.isEmpty()) {
            while (cur != null) {
                stack.push(cur);
                cur = cur.right;
            }

            cur = stack.pop();

            cur.val += addon;
            addon = cur.val;

            cur = cur.left;
        }
    }

}