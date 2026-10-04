# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        ahead = head
        curr = head

        while ahead and n > 0:
            ahead = ahead.next
            n -= 1

        if not ahead:
            return None

        ahead = ahead.next

        while curr and ahead:
            curr = curr.next
            ahead = ahead.next

        curr.next = curr.next.next

        return head