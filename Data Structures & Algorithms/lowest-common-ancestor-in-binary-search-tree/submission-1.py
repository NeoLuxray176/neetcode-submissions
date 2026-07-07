# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
  def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    # Since this is a search tree, we need to find a node such that its value is larger than p and smaller than q

    if p.val > q.val:
      p.val, q.val = q.val, p.val
    # Now p <= q

    def dfs(node: Optional[TreeNode]) -> Optional[TreeNode]:
      if not node:
        return None

      if p.val <= node.val and q.val >= node.val:
        return node

      leftVal = dfs(node.left)
      rightVal = dfs(node.right)

      if leftVal:
        return leftVal

      if rightVal:
        return rightVal

      print("Oh noes")
      return None

    return dfs(root)
