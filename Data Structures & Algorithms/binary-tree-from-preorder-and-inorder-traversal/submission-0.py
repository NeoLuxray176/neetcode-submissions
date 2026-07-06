class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None

        root = TreeNode(preorder[0])
        stack = [root]
        inIdx = 0

        for i in range(1, len(preorder)):
            node = TreeNode(preorder[i])

            # If the top of the stack hasn't matched inorder yet,
            # this node is the left child
            if stack[-1].val != inorder[inIdx]:
                stack[-1].left = node
                stack.append(node)
            else:
                # Pop until we find where to attach the right child
                while stack and stack[-1].val == inorder[inIdx]:
                    last = stack.pop()
                    inIdx += 1
                last.right = node
                stack.append(node)

        return root
