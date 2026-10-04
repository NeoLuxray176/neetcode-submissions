# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # General idea
        # Find the start to the second half
        # Split the two halves
        # Reverse second half
        # Then merge the two lists
        
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        two = slow.next
        slow.next = None
        prev, curr = None, two

        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        one, two = head, prev

        # Merge the two lists

        while one and two:
            tmp1, tmp2 = one.next, two.next

            one.next = two
            two.next = tmp1
            one = tmp1
            two = tmp2