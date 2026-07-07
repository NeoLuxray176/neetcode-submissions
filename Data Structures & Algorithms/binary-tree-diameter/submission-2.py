# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        mp = {None: (0, 0)}

        queue = deque()
        queue.append(root)

        while queue:
            node = queue[-1]
            
            if node.left and node.left not in mp:
                queue.append(node.left)
            elif node.right and node.right not in mp:
                queue.append(node.right)
            else:
                node = queue.pop()

                leftHeight, leftDiameter = mp[node.left]
                rightHeight, rightDiameter = mp[node.right]

                mp[node] = (1 + max(leftHeight, rightHeight), max(leftHeight + rightHeight, leftDiameter, rightDiameter))

        return mp[root][1]