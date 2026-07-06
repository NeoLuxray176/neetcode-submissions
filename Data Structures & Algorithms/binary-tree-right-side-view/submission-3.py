# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        # Salvaged: Storing (node, level) tuple in the stack
        stack = [(root, 0)]
        output = []
        
        # We use this to track if we have already seen a node at this depth
        seen_depths = set()

        while stack:
            # Salvaged: Pop node and its depth
            node, level = stack.pop()

            if node:
                # Logic Fix: Only add to output if this level is new to us
                if level not in seen_depths:
                    output.append(node.val)
                    seen_depths.add(level)
                
                # Logic Fix: Add LEFT first, then RIGHT. 
                # Because it's a stack (LIFO), RIGHT will be popped/visited first.
                # We also increment the level for the children.
                if node.left:
                    stack.append((node.left, level + 1))
                if node.right:
                    stack.append((node.right, level + 1))
            
        return output