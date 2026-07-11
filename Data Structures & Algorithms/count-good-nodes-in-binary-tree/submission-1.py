# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
  def goodNodes(self, root: TreeNode) -> int:

    # Explore all paths and remember the max val encountered on that path

    # DFS

    stack = deque()
    stack.append((root, root.val))

    res = 0

    while stack:
      (node, curr_max) = stack.pop()
    #   print(node.val, curr_max, node.val <= curr_max)

      if node.val >= curr_max:
        res += 1

      if node.left:
        stack.append((node.left, max(node.val, curr_max)))
      if node.right:
        stack.append((node.right, max(node.val, curr_max)))

    return res
