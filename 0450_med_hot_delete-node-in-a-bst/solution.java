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
    public TreeNode deleteNode(TreeNode root, int key) {
        if (root == null) {
            return null;
        }       

        if (root.val != key) {
            root.left = deleteNode(root.left, key);
            root.right = deleteNode(root.right, key);
            return root;
        } else {
            TreeNode left = root.left;
            TreeNode right = root.right;
            if(left == null && right == null) {
                return null;
            } else if (left != null && right == null) {
                return left;
            } else if (left == null && right != null) {
                return right;
            } else {
                // left != null && right != null
                TreeNode ptr = right;
                while (ptr.left != null) {
                    ptr = ptr.left;
                } 
                ptr.left = left;
                return right;
            }
        }
    }
}


class Solution2 {
    public TreeNode deleteNode(TreeNode root, int key) {
        if (root == null) {
            return null;
        }

        TreeNode parent = null;
        TreeNode cur = root;

        while (cur != null) {
            if (cur.val == key) {
                break;
            }
            parent = cur;
            if (key < cur.val) {
                cur = cur.left;
            } else {
                cur = cur.right;
            }
        }

        if (parent == null) {
            return deleteOneNode(cur);
        }

        if (parent.left != null && key == parent.left.val) {
            parent.left = deleteOneNode(cur);
        }
        if (parent.right != null && key == parent.right.val) {
            parent.right = deleteOneNode(cur);
        }

        return root;
        
    }

    private TreeNode deleteOneNode(TreeNode node) {
        if(node == null) {
            return null;
        }

        TreeNode left = node.left;
        TreeNode right = node.right;

        if(left == null && right == null) {
            return null;
        } else if(left != null && right == null) {
            return left;
        } else if(left == null && right != null) {
            return right;
        } else {
            // left != null && right != null
            TreeNode ptr = right;
            while(ptr.left != null) {
                ptr = ptr.left;
            }
            ptr.left = left;
            return right;
        }
    }
}