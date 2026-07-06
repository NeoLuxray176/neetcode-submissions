# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # 1. Find middle of the list
        # 2. reverse second half
        # 3. Merge the two lists

        slow, fast = head, head.next

        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next

        middle = slow
        # 2. Reverse second half
        second = slow.next
        prev = slow.next = None

        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp


        first, second = head, prev

        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2