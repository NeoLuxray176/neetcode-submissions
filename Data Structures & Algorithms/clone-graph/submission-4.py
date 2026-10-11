"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # DFS on the graph first to discover all nodes
        # then a second iteration to discover all neighbors
        # Use a hashmap to map old nodes to new nodes

        if not node:
            return node

        stack = [node]
        dic = {}
        visit = set()

        while stack:
            curr = stack.pop()

            if curr in visit:
                continue
            visit.add(curr)

            if curr not in dic:
                dic[curr] = Node(val=curr.val)
            for neighbor in curr.neighbors:
                if neighbor not in dic:
                    dic[neighbor] = Node(val=neighbor.val)
                
                dic[curr].neighbors.append(dic[neighbor])
                # dic[neighbor].neighbors.append(dic[curr])
                
                if neighbor not in visit:
                    stack.append(neighbor)

        return dic[node]
                        