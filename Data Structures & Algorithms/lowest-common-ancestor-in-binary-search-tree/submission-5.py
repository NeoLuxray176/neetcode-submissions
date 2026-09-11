# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # This is a binary search tree
        # So we need to find a node such that its value is larger or equal than p and smaller or equal than q


        def dfs(node : TreeNode) -> TreeNode:
            if not node:
                return None

            if p.val <= node.val <= q.val:
                return node
            if q.val <= node.val <= p.val:
                return node

            left_node = dfs(node.left)
            right_node = dfs(node.right)

            if left_node:
                return left_node
            if right_node:
                return right_node

        res = dfs(root)
        return res