# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        output = 0
        stack = deque()

        if root:
            # output += 1
            stack.append((root, root.val))

        while stack:
            curr_node, max_from_root = stack.pop()
            curr_max = max(max_from_root, curr_node.val)

            if curr_node and curr_node.val >= max_from_root:
                print(f"At {curr_node.val} we are the largest value until the root.")
                output += 1
            elif curr_node:
                print(f"At {curr_node.val} we are smaller than {max_from_root}")

            print(f"Next max is {curr_max}")
            if curr_node.left:
                stack.append((curr_node.left, curr_max))
            if curr_node.right:
                stack.append((curr_node.right, curr_max))
        
        return output

            
        


        