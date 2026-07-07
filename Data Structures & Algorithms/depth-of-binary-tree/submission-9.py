# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Recursive
        # Base case, no children, depth is 0
        # Recursion, increase depth by one

        if not root:
            return 0

        left_depth = 1 + self.maxDepth(root.left)
        right_depth = 1+ self.maxDepth(root.right)

        return max(left_depth, right_depth)
            