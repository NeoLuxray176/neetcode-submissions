# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def dfs(p_node : Optional[TreeNode], q_node : Optional[TreeNode]):
            if not p_node and not q_node:
                return True

            if not p_node:
                return False

            if not q_node:
                return False

            if p_node.val != q_node.val:
                return False

            left_sol = dfs(p_node.left, q_node.left)
            right_sol = dfs(p_node.right, q_node.right)

            return left_sol and right_sol

        return dfs(p, q)
