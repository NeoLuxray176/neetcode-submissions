# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Let's do dfs and store the max depth encountered

        if not root:
            return 0

        queue = []
        queue.append((root, 1))

        res = 0

        while queue:
            node, depth = queue.pop()

            if node.left:
                queue.append((node.left, depth + 1))
            if node.right:
                queue.append((node.right, depth + 1))

            res = max(res, depth)

        return res