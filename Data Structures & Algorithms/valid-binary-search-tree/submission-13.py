# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # left subtree is smaller than the current key, smaller than the minimum encountered so far
        # right subtree is larger than the current key, larger than the max encountered so far

        if not root:
            return True

        stack = [[root, root.val]]

        while stack:
            node, value = stack.pop()

            if node.left:
                if node.left.val >= node.val or node.left.val >= value:
                    return False
            if node.right:
                if node.right.val <= node.val or node.right.val <= value:
                    return False

            if node.left:
                stack.append([node.left, min(value, node.left.val)])
            if node.right:
                stack.append([node.right, max(value, node.right.val)])

        return True