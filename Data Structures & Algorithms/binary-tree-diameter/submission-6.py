# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        # The diameter of the subtree of node n is the height of its two subtrees


        def dfs(node : Optional[TreeNode]) -> List[int]:
            if not node:
                return [0, 0] # Height, maximum diameter

            left = dfs(node.left)
            right = dfs(node.right)

            my_height = 1 + max(left[0], right[0])
            my_diameter = left[0] + right[0]
            max_diameter = max(left[1], right[1], my_diameter)

            return [my_height, max_diameter]

        return dfs(root)[1]

            
