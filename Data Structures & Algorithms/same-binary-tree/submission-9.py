# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        # Two binary trees are equivalent if their left and right subtrees are equivalent
        # And these two nodes are equivalent

        # Base case, no children
        # Recursive case: value is the same

        if not p and not q:
            return True

        if not p:
            return False

        if not q:
            return False

        if p.val != q.val:
            return False

        leftSame = self.isSameTree(p.left, q.left)
        rightSame = self.isSameTree(p.right, q.right)

        return leftSame and rightSame