# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        p_stack = [p]
        q_stack = [q]

        while p_stack and q_stack:
            p_node = p_stack.pop()
            q_node = q_stack.pop()

            if not p_node and q_node or p_node and not q_node:
                return False
            
            if p_node and q_node:
                if p_node.val != q_node.val:
                    return False
            else:
                break

            if p_node.left:
                if not q_node.left:
                    return False
                else:
                    p_stack.append(p_node.left)
                    q_stack.append(q_node.left)

            if p_node.right:
                if not q_node.right:
                    return False
                else:
                    p_stack.append(p_node.right)
                    q_stack.append(q_node.right)

        return len(p_stack) == len(q_stack)
