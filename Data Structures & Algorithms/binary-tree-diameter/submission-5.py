# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # The diameter is the sum of the heights of the left and right subtrees

        def dfs(node : Optional[TreeNode]):
            if not node:
                return [0, 0]
            
            left = dfs(node.left)
            right = dfs(node.right)

            height = 1 + max(left[0], right[0])
            diameter = max(left[0] + right[0], left[1], right[1])

            return [height, diameter]

        return dfs(root)[1]
            
