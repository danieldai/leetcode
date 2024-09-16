# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        r = root

        while not (p.val <= r.val <= q.val or q.val <= r.val <= p.val):
        
            if p.val < r.val and q.val < r.val:
                r = r.left
            if p.val > r.val and q.val > r.val:
                r = r.right

        return r
    

class Solution2:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        
        if q.val < root.val and p.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif q.val > root.val and p.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root