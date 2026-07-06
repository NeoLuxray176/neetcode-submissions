# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        real_head = head
        carry = 0
        while l1 != None or l2 != None:
            l = l1.val if l1 != None else 0
            r = l2.val if l2 != None else 0
            addy = (r + l) + carry
            carry = 0

            if addy > 9:
                addy = addy % 10
                carry = 1
            
            head.val = addy
            if (l1.next != None or l2.next != None):
                head.next = ListNode()
                head = head.next
            if l1 != None:
                l1 = l1.next
            if l2 != None:
                l2 = l2.next

        if carry > 0:
            head.next = ListNode()
            head = head.next
            head.val = carry
        
        return real_head