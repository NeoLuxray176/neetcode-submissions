# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # We can do a full level view but only ever store the right-most node
        # per level.
        # Can we do better?
        # No, we need to traverse the full tree because we cannot know in advance whether
        # there are unused nodes. Consider the case where we have a level
        # with a single child on the very left side of the three. To know about that child
        # we will have to have traversed the full left side of the tree.

        # We do BFS on the tree
        # We store in a stack, the next node to be traversed and its level (where root is
        # at level 0, it's children at level 1 and so on ...)
        # We store per level the value of the rightmost node in an array of length level
        # This means that we explore the left side first and then overwrite if there is a
        # node on the right

        if not root:
            return []

        stack = []
        stack.append((0, root))
        res = []

        while stack:
            level, node = stack.pop()

            if len(res) <= level:
                res.append(node.val)
            else:
                res[level] = node.val

            if node.right:
                stack.append((level + 1, node.right))
            if node.left:
                stack.append((level + 1, node.left))

        return res
            
