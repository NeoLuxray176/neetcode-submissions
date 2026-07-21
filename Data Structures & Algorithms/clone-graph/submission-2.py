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
            return None

        res = Node(val=node.val)
        hmap = {}
        hmap[node] = res
        queue = [node]

        while queue:
            curr_node = queue.pop()

            for neighbor in curr_node.neighbors:
                if neighbor not in hmap:
                    hmap[neighbor] = Node(val=neighbor.val)
                    queue.append(neighbor)
                hmap[curr_node].neighbors.append(hmap[neighbor])
        
        return res