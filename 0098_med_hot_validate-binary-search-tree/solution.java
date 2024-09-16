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
    public boolean isValidBST(TreeNode root) {
        List<Integer> values = inorder(root);

        if(values.size() <= 1) {
            return true;
        }

        for(int i = 0; i < values.size() - 1; i++) {
            if(values.get(i) >= values.get(i+1)) {
                return false;
            }
        }

        return true;
    }

    public List<Integer> inorder(TreeNode root) {
        List<Integer> result = new ArrayList<>();

        if(root == null) {
            return result;
        }

        result.addAll(inorder(root.left));
        result.add(root.val);
        result.addAll(inorder(root.right));

        return result;
    }
}

class Solution2 {

    boolean isValid = true;
    TreeNode prev = null;

    public boolean isValidBST(TreeNode root) {
        inorder(root);
        return isValid;
    }

    public void inorder(TreeNode root) {
        if (root == null) {
            return;
        }

        TreeNode cur = root;
        Deque<TreeNode> stack = new LinkedList<>();

        while (cur != null || !stack.isEmpty()) {
            while (cur != null) {
                stack.push(cur);
                cur = cur.left;
            }
            
            cur = stack.pop();

            if(prev != null) {
                if(!(cur.val > prev.val)) {
                    isValid = false;
                    return;
                }
            }
            prev = cur;

            cur = cur.right;
        }
    }
}