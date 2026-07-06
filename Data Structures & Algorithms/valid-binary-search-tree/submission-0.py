# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        stack = deque()

        if root:
            stack.append(root)

        while stack:
            curr = stack.pop()

            if not curr:
                continue

            if curr.left:
                if curr.left.val > curr.val:
                    return False
                stack.append(curr.left)
            if curr.right:
                if curr.right.val < curr.val:
                    return False
                stack.append(curr.right)
            
        
        return True
                