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

        queue = deque()
        queue.append((root, 0))

        res = []

        while queue:
            (root, height) = queue.popleft()

            if len(res) > height:
                res[height].append(root.val)
            else:
                res.append([root.val])

            if root.left:
                queue.append((root.left, height + 1))
            if root.right:
                queue.append((root.right, height + 1))

        return res


            