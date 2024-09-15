import java.util.ArrayList;
import java.util.List;

/**
 * Definition for a binary tree node.
 */

 public class TreeNode {
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
    public List<String> binaryTreePaths(TreeNode root) {
        if(root == null) {
            return new ArrayList<>();
        }

        List<String> result = new ArrayList<>();
        
        for(String suffix : binaryTreePaths(root.left)) {
            result.add(String.format("%s->%s", root.val, suffix));
        }

        for(String suffix : binaryTreePaths(root.right)) {
            result.add(String.format("%s->%s", root.val, suffix));
        }

        if(result.isEmpty()) {
            result.add(String.valueOf(root.val));
        }

        return result;
    }
}