# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left = dummy
        right = head

        # Go n-steps to the right
        while n > 0:
            right = right.next
            n -= 1

        # Left will now point to the n-th node from the right because right was
        # n steps ahead
        while right:
            left = left.next
            right = right.next

        left.next = left.next.next
        return dummy.next

