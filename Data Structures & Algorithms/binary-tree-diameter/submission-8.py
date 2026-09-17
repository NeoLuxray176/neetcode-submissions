# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # The diameter at node n is the height of its two subtrees
        # Do DFS and calculate the current height of the node as well as the maximum diameter encountered so far
        # return a tuple

        def dfs(root : Optional[TreeNode]) -> List[int]: # [height, max_diameter]
            if not root:
                return [0, 0] # height, max_diameter are both zero

            left, right = dfs(root.left), dfs(root.right)

            myHeight = 1 + max(left[0], right[0])
            myDiameter = left[0] + right[0]
            max_diameter = max(myDiameter, left[1], right[1])

            return [myHeight, myDiameter]

        return dfs(root)[1]
