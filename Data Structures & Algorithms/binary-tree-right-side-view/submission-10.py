# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        res = []

        stack = [[root, 1]]

        while stack:
            node, level = stack.pop()

            if len(res) < level:
                res.append(node.val)

            if node.left:
                stack.append([node.left, level + 1])
            if node.right:
                stack.append([node.right, level + 1])

        return res