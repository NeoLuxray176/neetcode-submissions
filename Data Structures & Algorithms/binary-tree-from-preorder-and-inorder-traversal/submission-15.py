class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        root = TreeNode(val=preorder[0])
        middle = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1: middle + 1], inorder[:middle])
        root.right = self.buildTree(preorder[middle + 1:], inorder[middle + 1:])

        return root