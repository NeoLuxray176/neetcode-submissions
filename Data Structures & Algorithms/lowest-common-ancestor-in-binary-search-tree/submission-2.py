# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
  def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    # Since this is a search tree, we need to find a node such that its value is larger than p and smaller than q

    node = root

    lo, hi = min(p.val, q.val), max(p.val, q.val)

    while node:
        if lo > node.val:
            node = node.right
        elif hi < node.val:
            node = node.left
        else:
            return node

    return None
