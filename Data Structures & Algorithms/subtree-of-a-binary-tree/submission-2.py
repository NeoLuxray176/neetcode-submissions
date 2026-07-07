# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def dfs(node : Optional[TreeNode], subRoot : Optional[TreeNode]):
            if not node and not subRoot:
                return True
            
            if not node:
                return False
            
            if not subRoot:
                return False

            if node.val != subRoot.val:
                left_equal = dfs(node.left, subRoot)
                right_equal = dfs(node.right, subRoot)

                return left_equal or right_equal    

            left_equal = dfs(node.left, subRoot.left)
            right_equal = dfs(node.right, subRoot.right)

            return left_equal and right_equal

        return dfs(root, subRoot)

        