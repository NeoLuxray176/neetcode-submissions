# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
  def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    # Since this is a search tree, we need to find a node such that its value is larger than p and smaller than q

    if p.val <= root.val and q.val >= root.val:
        return root
    if p.val >= root.val and q.val <= root.val:
        return root


    if root.left:
        lhs = self.lowestCommonAncestor(root.left, p, q)
        if lhs:
            return lhs
    
    if root.right:
        rhs = self.lowestCommonAncestor(root.right, p, q)
        if rhs:
            return rhs
    
    return None