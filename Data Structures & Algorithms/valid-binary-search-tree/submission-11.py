class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        # Let's do BFS
        if not root:
            return True

        queue = deque()
        queue.append((float("-inf"), float("inf"), root))

        while queue:
            left_max, right_max, node = queue.popleft()

            if not left_max < node.val < right_max:
                return False

            if node.left:
                queue.append((left_max, node.val, node.left))

            if node.right:
                queue.append((node.val, right_max, node.right))

        return True