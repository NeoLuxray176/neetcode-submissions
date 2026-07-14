class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        if not preorder:
            return None

        root = TreeNode(preorder[0])

        # Find root position in inorder
        pos = inorder.index(root.val)

        # Build left and right subtrees
        root.left = self.buildTree(preorder[1:pos + 1], inorder[:pos])
        root.right = self.buildTree(preorder[pos + 1:], inorder[pos + 1:])

        return root