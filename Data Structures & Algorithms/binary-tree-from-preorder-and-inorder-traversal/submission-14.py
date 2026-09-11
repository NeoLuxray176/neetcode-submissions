# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Morris traversal allows us to build the tree iteratively without using a recursion 
        # stack. The idea is to use the right pointers of nodes to temporarily store parent 
        # references, simulating the call stack. We build nodes as we iterate through preorder, 
        # connecting them via left/right pointers. When we finish a left subtree (detected by 
        # matching the inorder sequence), we restore the original structure by clearing temporary 
        # links and moving up the tree.
        i, j, n = 0, 0, len(preorder)

        head = TreeNode(None)
        curr = head
        
        while i < n and j < n:
            curr.right = TreeNode(preorder[i], right = curr.right)
            curr = curr.right
            i += 1

            while i < n and curr.val != inorder[j]:
                curr.left = TreeNode(preorder[i], right=curr)
                curr = curr.left
                i += 1
            j += 1
            # Move up the tree and clear the parent links
            while curr.right and j < n and curr.right.val == inorder[j]:
                curr.right, curr = None, curr.right
                j += 1

        return head.right