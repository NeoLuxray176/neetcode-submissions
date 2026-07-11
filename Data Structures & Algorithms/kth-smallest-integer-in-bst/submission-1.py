# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # The smallest value is in the bottom left node
        # The next smallest value is in the parent of the bottom left node
        # The next smallest value is in the right child of the parent of the bottom left node

        # This is exactly the order DFS visits the nodes

        if not root:
            return -1

        stack = [(root, 0)]
        curr = root

        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()
            k -= 1
            if k == 0:
                return curr.val
            curr = curr.right


