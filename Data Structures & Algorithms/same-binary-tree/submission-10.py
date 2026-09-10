# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def dfs(p : Optional[Treenode], q : Optional[Treenode]) -> bool:
            if not p and not q:
                return True
            if p and q and p.val != q.val:
                return False
            if not p:
                return False
            if not q:
                return False

            return dfs(p.left, q.left) and dfs(p.right, q.right)

        return dfs(p, q)
