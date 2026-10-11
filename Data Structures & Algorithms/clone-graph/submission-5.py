"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node
        dic = {}
        visited = set()


        stack = [node]

        while stack:
            curr = stack.pop()

            if curr in visited:
                continue
            visited.add(curr)

            if curr not in dic:
                dic[curr] = Node(val=curr.val)

            for neighbor in curr.neighbors:
                if neighbor not in dic:
                    dic[neighbor] = Node(val=neighbor.val)
                dic[curr].neighbors.append(dic[neighbor])

                stack.append(neighbor)

        return dic[node]