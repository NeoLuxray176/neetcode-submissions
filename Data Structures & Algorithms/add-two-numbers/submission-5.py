# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0

        dummy = ListNode(val=-1)

        curr = dummy
        while l1 or l2:
            new_val = carry
            if l1:
                new_val += l1.val
            if l2:
                new_val += l2.val
            carry = 0

            if new_val > 9:
                carry = 1
                new_val = new_val % 10
            
            curr.next = ListNode(val=new_val)
            curr = curr.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        if carry:
            curr.next = ListNode(val=carry)

        return dummy.next