# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return -1


        queue = []
        curr = root

        while queue or curr:
            while curr:
                queue.append(curr)
                curr = curr.left
            curr = queue.pop()
            k -= 1
            if k == 0:
                return curr.val
            
            curr = curr.right

        return -1