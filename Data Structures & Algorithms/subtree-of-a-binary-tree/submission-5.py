# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
  def isSameTree(self, p : Optional[TreeNode], q : Optional[TreeNode]) -> bool:
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

  def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
    if not root and not subRoot:
      return True

    if not root:
      return False

    if not subRoot:
      return False

    return self.isSameTree(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)