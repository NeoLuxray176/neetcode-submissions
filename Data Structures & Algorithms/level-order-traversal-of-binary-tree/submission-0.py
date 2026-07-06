# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        stack = collections.deque()
        stack.append((root, 0))

        output = []

        while stack:
            node, level = stack.popleft()

            if not node:
                continue

            if len(output) > level:
                output[level].append(node.val)
            else:
                output.append([node.val])

            if node.left:
                stack.append((node.left, level + 1))
            if node.right:
                stack.append((node.right, level + 1))
        
        return output