# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        res = 0
        stack = [[root, -101]]

        while stack:
            node, prevMax = stack.pop()

            # print(f"{node.val} is bigger than {prevMax}")
            if node.val >= prevMax:
                res += 1

            if node.left:
                stack.append([node.left, max(prevMax, node.val)])
            if node.right:
                stack.append([node.right, max(prevMax, node.val)])

        return res