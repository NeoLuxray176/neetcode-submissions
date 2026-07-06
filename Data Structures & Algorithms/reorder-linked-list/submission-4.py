# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # The first half is in order
        # The second half is reversed
        # The two are mixed in together

        # First reverse the second half of the list
        # Then in-order merge the two halfes

        # Find the middle of the list

        slow, fast = head, head

        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        middle = slow.next # Double check that this is actually the middle
        slow.next = None
        
        # Reverse second half
        prev, curr = None, middle
        while curr:
            curr.next, prev, curr = prev, curr, curr.next

        first, second = head, prev
        while second:
            first.next, second.next, first, second = second, first.next, first.next, second.next
        
