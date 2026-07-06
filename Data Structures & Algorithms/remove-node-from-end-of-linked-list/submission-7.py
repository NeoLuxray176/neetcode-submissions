# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        dummy = ListNode(next=head)
        fast = dummy

        while n >= 0 and fast:
            fast = fast.next
            n -= 1

        slow = dummy

        while slow and fast:
            slow = slow.next
            fast = fast.next

        if slow and slow.next:
            slow.next = slow.next.next

        return dummy.next

