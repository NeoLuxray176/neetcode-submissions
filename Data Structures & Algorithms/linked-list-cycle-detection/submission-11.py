# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        if not head.next and head.next != head:
            return False

        slow, fast = head, head.next.next

        while slow and fast:
            if slow == fast:
                return True

            slow, fast = slow.next, fast.next.next

        return False