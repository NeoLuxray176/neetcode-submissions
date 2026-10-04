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

        stack = [[root, 0]]

        while stack:
            node, path_sum = stack.pop()

            if not node.left and not node.right and path_sum + node.val == targetSum:
                return True

            if node.left:
                stack.append([node.left, path_sum + node.val])
            if node.right:
                stack.append([node.right, path_sum + node.val])

        return False