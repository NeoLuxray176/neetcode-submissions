class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None

        root = TreeNode(preorder[0])
        stack = [root]
        inIdx = 0

        for val in preorder[1:]:
            node = stack[-1]
            # Build left subtree ith the preorder value until we hit the same value
            # in the inorder array. Then we know that we need to start building the right subtree
            if node.val != inorder[inIdx]:
                node.left = TreeNode(val)
                stack.append(node.left)
            else:
                # Build right subtree
                # We are in the right subtree scenario for as long as
                # the order in the stack (which comes from the preorder array)
                #  agrees with the inorder array
                while stack and stack[-1].val == inorder[inIdx]:
                    node = stack.pop()
                    inIdx += 1
                node.right = TreeNode(val)
                stack.append(node.right)

        return root