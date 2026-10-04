# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        
        stack = [(root, 0)]

        while stack:
            curr, path_sum = stack.pop()

            if not curr.left and not curr.right and path_sum + curr.val == targetSum:
                return True
            
            if curr.left:
                stack.append((curr.left, path_sum + curr.val))
            if curr.right:
                stack.append((curr.right, path_sum + curr.val))

        return False
