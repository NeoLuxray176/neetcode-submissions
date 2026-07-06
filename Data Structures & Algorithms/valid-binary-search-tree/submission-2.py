import math

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        # Stack stores tuples of: (node, lower_bound, upper_bound)
        # We start with negative infinity to positive infinity
        stack = [(root, -math.inf, math.inf)]
        
        while stack:
            node, low, high = stack.pop()
            
            if not node:
                continue
            
            # 1. The Critical Check: 
            # The current node's value must stay strictly within the inherited bounds
            if not (low < node.val < high):
                return False
            
            # 2. Push children with updated bounds
            # Going Right: The node must be > current val (low bound increases)
            stack.append((node.right, node.val, high))
            
            # Going Left: The node must be < current val (high bound decreases)
            stack.append((node.left, low, node.val))
            
        return True