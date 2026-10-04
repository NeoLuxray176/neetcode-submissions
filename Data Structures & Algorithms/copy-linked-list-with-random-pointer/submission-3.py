"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        dummy = Node(x=-1)
        new_curr = dummy
        curr = head

        mapping = {}

        while curr:
            new_curr.next = Node(x=curr.val)
            mapping[curr] = new_curr.next
            new_curr = new_curr.next
            curr = curr.next

        curr = head
        new_curr = dummy.next

        while curr:
            if curr.random:
                new_curr.random = mapping[curr.random]
            curr = curr.next
            new_curr = new_curr.next

        return dummy.next

