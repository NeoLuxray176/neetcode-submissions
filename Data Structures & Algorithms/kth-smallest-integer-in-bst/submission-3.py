# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # Let's see how this would work with a depth first search.
        # Once we are at the first node with no children, a leaf, then we know 
        # that this is the smallest value. Then going up we now that our parent is
        # the second smallest value, and it's children are the next smaller values.
        # So we can count down k from there until it is one

        if not root:
            return -1

        curr = root
        stack = []

        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            k -= 1
            if k == 0:
                return curr.val
            curr = curr.right
            

