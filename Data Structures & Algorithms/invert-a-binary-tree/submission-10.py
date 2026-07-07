from collections import deque 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # at each node we switch the left and right child

        if not root:
            return root

        stack = deque()
        stack.append(root)

        while stack:
            node = stack.popleft()

            if node.left:
                stack.append(node.left)

            if node.right:
                stack.append(node.right)

            node.left, node.right = node.right, node.left

        return root
