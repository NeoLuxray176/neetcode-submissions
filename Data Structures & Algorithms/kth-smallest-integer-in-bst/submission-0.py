# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = deque()
        curr = root
        
        while stack or curr:
            # 1. Go as deep left as possible
            while curr:
                stack.append(curr)
                curr = curr.left
            
            # 2. Pop the element (this is the next smallest)
            curr = stack.pop()
            k -= 1
            
            # 3. If k is 0, we found our target
            if k == 0:
                return curr.val
            
            # 4. Move to the right child
            curr = curr.right
            
        return -1