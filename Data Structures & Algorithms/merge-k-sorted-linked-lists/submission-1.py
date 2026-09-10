# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class ComparableNode:
    def __init__(self, node):
        self.node = node

    def __lt__(self, other):
        return self.node.val < other.node.val

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None

        dummy = ListNode(0)
        curr = dummy
        minHeap = []

        for head in lists:
            if head:
                heapq.heappush(minHeap, ComparableNode(head))

        while minHeap:
            comparable_node = heapq.heappop(minHeap)
            curr.next = comparable_node.node
            curr = curr.next

            if comparable_node.node.next:
                heapq.heappush(minHeap, ComparableNode(comparable_node.node.next))

        return dummy.next
