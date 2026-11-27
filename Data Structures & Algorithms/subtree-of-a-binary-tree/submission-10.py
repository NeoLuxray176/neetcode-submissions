# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def is_same(p : Optional[TreeNode], q : Optional[TreeNode]):
            if not p and q:
                return False
            if p and not q:
                return False
            if not p and not q:
                return True
            if p.val != q.val:
                return False
            return is_same(p.left, q.left) and is_same(p.right, q.right)
        
        if is_same(root, subRoot):
            return True
        if not root:
            return False
        
        return is_same(root.left, subRoot) or is_same(root.right, subRoot)