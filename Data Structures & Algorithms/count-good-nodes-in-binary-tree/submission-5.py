# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # Let's do DFS and keep track of the maximum encountered so far
        # The root is always good

        res = 0

        stack = []
        stack.append((root.val, root))

        while stack:
            curr_max, node = stack.pop()

            if curr_max <= node.val:
                res += 1
            curr_max = max(curr_max, node.val)

            if node.left:
                stack.append((curr_max, node.left))
            if node.right:
                stack.append((curr_max, node.right))

        return res