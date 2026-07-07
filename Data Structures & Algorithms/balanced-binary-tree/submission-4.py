# Definition for a binary tree node.
# class TreeNode: 
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # We are balanced if at any node the two subtrees's height differs by at most one

        # Calculate the height of every node
        # Check the heights of the two subtrees

        def dfs(node: Optional[TreeNode]) -> int:
            if not node:
                return 0

            leftHeight = dfs(node.left)
            rightHeight = dfs(node.right)

            if leftHeight == -1 or rightHeight == -1 or abs(leftHeight - rightHeight) > 1:
                return -1

            return 1 + max(leftHeight, rightHeight)

        return dfs(root) != -1