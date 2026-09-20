# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        best = float("-inf")

        def dfs(node : Optional[TreeNode]) -> int:
            nonlocal best
            if not node:
                return 0

            left = max(0, dfs(node.left)) # only use left if it increases the max sum
            right = max(0, dfs(node.right))
            best = max(best, node.val + left + right) # path through the current node
            
            return node.val + max(left, right) # we can only use node once, so choose the larger of the two paths

        dfs(root)
        return best