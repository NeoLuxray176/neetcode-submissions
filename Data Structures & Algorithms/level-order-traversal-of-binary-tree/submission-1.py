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

        queue = deque()
        queue.append((0, root))

        while queue:
            (level, node) = queue.popleft()

            if node.left:
                queue.append((1 + level, node.left))

            if node.right:
                queue.append((1 + level, node.right))

            if level < len(res):
                res[level].append(node.val)
            else:
                res.append([node.val])
        
        return res

            