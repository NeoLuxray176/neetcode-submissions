class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(node, number):
            if node is None:
                return 0

            number = number * 10 + node.val

            if node.left is None and node.right is None:
                return number

            return dfs(node.left, number) + dfs(node.right, number)

        return dfs(root, 0)