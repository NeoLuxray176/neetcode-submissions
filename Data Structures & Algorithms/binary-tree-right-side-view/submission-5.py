# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        view = []
        queue = deque([(root, 0)])
        while queue:
            node, depth = queue.popleft()
            if depth == len(view):
                view.append(node.val)   # first node reaching this depth
            else:
                view[depth] = node.val  # later visit = further right
            if node.left:  queue.append((node.left, depth + 1))
            if node.right: queue.append((node.right, depth + 1))
        return view