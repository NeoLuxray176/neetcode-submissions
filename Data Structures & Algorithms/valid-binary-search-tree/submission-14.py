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

        stack = [[root, float("-inf"), float("inf")]]

        while stack:
            node, lower_bound, upper_bound = stack.pop()

            if upper_bound <= node.val or lower_bound >= node.val:
                    return False

            if node.left:
                stack.append([node.left, lower_bound, node.val])
            if node.right:
                stack.append([node.right, node.val, upper_bound])

        return True