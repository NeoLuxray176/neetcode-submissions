# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        res = []

        # Let's do bfs here
        stack = []
        stack.append((0, root))

        while stack:
            level, node = stack.pop()
            if len(res) <= level:
                res.append([])
            res[level].append(node.val)


            if node.right:
                stack.append((level + 1, node.right))
            if node.left:
                stack.append((level + 1, node.left))

        return res



        