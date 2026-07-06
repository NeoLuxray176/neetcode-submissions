# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack = [(p, q)]

        while stack:
            p_node, q_node = stack.pop()

            if not p_node and not q_node:
                continue
            if not p_node or not q_node or p_node.val != q_node.val:
                return False

            stack.append((p_node.left, q_node.left))
            stack.append((p_node.right, q_node.right))

        return True