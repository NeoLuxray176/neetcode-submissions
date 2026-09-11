# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        # Let's do BFS
        if not root:
            return True

        queue = deque()
        queue.append(root)

        while queue:
            node = queue.popleft()

            if node.left:
                if node.val <= node.left.val:
                    return False
                queue.append(node.left)
            if node.right:
                if node.val >= node.right.val:
                    return False
                queue.append(node.right)

        return True
        