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
        
        per_level = []

        stack = deque()
        stack.append((root, 0))

        while stack:
            (node, height) = stack.popleft()

            if len(per_level) > height:
                per_level[height].append(node.val)
            else:
                per_level.append([node.val])

            if node.left:
                stack.append((node.left, height + 1))
            if node.right:
                stack.append((node.right, height + 1))
        
        res = []
        for level in per_level:
            res.append(level[-1])

        return res