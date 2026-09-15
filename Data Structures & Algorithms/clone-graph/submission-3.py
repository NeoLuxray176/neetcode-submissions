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

        queue = [node]
        hmap = {}
        res = Node(val=node.val)
        hmap[node] = res

        while queue:
            curr_node = queue.pop()
            if curr_node not in hmap:
                new_node = Node(val=curr_node.val)
                hmap[curr_node] = new_node
            
            for neighbor in curr_node.neighbors:
                if neighbor not in hmap:
                    new_node = Node(val=neighbor.val)
                    hmap[neighbor] = new_node
                    queue.append(neighbor)
                hmap[curr_node].neighbors.append(hmap[neighbor])

        return res