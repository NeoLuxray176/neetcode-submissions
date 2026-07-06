# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        stack = [root]

        while stack:
            node = stack.pop()
            
            if node.left and node.val > p.val and node.val > q.val:
                stack.append(node.left)
            if node.right and node.val < p.val and node.val < q.val:
                stack.append(node.right)
            if node.val >= p.val and node.val <= q.val:
                return node
            if node.val <= p.val and node.val >= q.val:
                return node
