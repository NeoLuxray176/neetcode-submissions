# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        # Task
        # Compute the number along the paths to the leaves and sum up all numbers
        # A number is generated using the values of the leaves with each value contributing a digit

        # Constraints
        # only numbers from 0 to 9
        # leading zeros need to be handled

        # General Idea
        # Do DFS Keep track of the current number
        # in each node multiply the number by ten and add the current value, pass it on to the next node

        res = 0

        if not root:
            return res

        stack = [(root, 0)]

        while stack:
            node, curr_num = stack.pop()

            curr_num = curr_num * 10 + node.val

            if not node.left and not node.right:
                res += curr_num
                continue

            if node.left:
                stack.append((node.left, curr_num))
            if node.right:
                stack.append((node.right, curr_num))

        return res


        

