class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_idx = {val: i for i, val in enumerate(inorder)}
        pre_iter = iter(preorder)

        def helper(left, right):
            if left > right:
                return None
            val = next(pre_iter)
            root = TreeNode(val)
            middle = inorder_idx[val]
            root.left = helper(left, middle - 1)
            root.right = helper(middle + 1, right)
            return root

        return helper(0, len(inorder) - 1)