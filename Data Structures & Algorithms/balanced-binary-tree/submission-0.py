# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        stack = [(root, False)]
        depths = {}

        while stack:
            node, visited = stack.pop()
            if not node:
                continue
            
            if visited:
                # Step 2: Children are processed. Check balance now.
                left = depths.get(node.left, 0)
                right = depths.get(node.right, 0)

                if abs(left - right) > 1:
                    return False

                depths[node] = 1 + max(left, right)
            else:
                # Step 1: First time seeing node. 
                # Mark as visited and push children (Right first, so Left processes first)
                stack.append((node, True))
                stack.append((node.right, False))
                stack.append((node.left, False))

        return True