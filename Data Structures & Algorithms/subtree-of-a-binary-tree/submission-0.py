# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        stack = [(root, None)]
        subnode_init = False
        while stack:
            node, subnode = stack.pop()
            if node and subnode:
                print(f"{node.val} {subnode.val}")
            elif node:
                print(f"{node.val} {subnode}")
            else:
                print(f"{node} {subnode}")

            if node and subnode and node.val != subnode.val:
                return False
            
            if node and subnode and node.left != subnode.left:
                return False
            
            if node and subnode and node.right != subnode.right:
                return False
            
            if not subnode:
                subnode = subRoot
            
            if node and subnode and node.val == subRoot.val:
                subnode_init = True
                stack.append((node.left, subnode.left))
                stack.append((node.right, subnode.right))
            elif node:
                stack.append((node.left, None))
                stack.append((node.right, None))
        
        return subnode_init