# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        index_map = {value : i   for i, value in enumerate(inorder)}
        pre_iter = iter(preorder)

        def helper(left, right):
            if left > right:
                return
            val = next(pre_iter)
            middle = index_map[val]
            root = TreeNode(val=val)
            root.left = helper(left, middle - 1)
            root.right = helper(middle + 1, right)
            return root

        return helper(0, len(preorder) - 1)