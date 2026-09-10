# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        fast = dummy

        while fast and n >= 0:
            fast = fast.next
            n -= 1

        slow, fast = dummy, fast
        while fast:
            slow, fast = slow.next, fast.next

        if slow and slow.next:
            slow.next = slow.next.next

        return dummy.next
            