# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        ahead = head
        curr = dummy

        while ahead and n > 0:
            ahead = ahead.next
            n -= 1

        while curr and ahead:
            curr = curr.next
            ahead = ahead.next

        curr.next = curr.next.next

        return dummy.next