# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        head = TreeNode(None)
        curr = head
        i, j, n = 0, 0, len(preorder)
        while i < n and j < n:
            # Go right and then as far left as possible
            curr.right = TreeNode(preorder[i], right = curr.right)
            curr = curr.right
            i += 1
            # Add all nodes on the left until we have finished building the left side
            # of the subtree which is indicated by the inorder order disagreeing
            while i < n and curr.val != inorder[j]:
                curr.left = TreeNode(preorder[i], right=curr)
                curr = curr.left
                i += 1
            j += 1
            # Go right until we find a value that we have not yet added to the tree
            # then continue with the next iteration of the outer loop which adds the
            # right side of the tree
            while curr.right and j < n and curr.right.val == inorder[j]:
                curr.right, curr = None, curr.right
                # prev = curr.right
                # curr.right = None
                # curr = prev
                j += 1

        return head.right