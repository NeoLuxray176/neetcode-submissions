import math

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # For each root and left and right subtree
        # All nodes on the left subtree are smaller than the roots value
        # All nodes on the right subtree are larger than the roots value

        stack = deque()
        # stack.append((root, float('-inf'), float('inf')))
        stack.append((root, -math.inf, math.inf))

        while stack:
            (node, low, high) = stack.pop()

            if not (low < node.val < high):
                print(low, node.val, high)
                return False

            if node.left:
                stack.append((node.left, low, root.val))
            if node.right:
                stack.append((node.right, node.val, high))

        return True
