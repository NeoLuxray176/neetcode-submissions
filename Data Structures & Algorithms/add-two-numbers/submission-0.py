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
        while l1 != None and l2 != None:
            addy = (l1.val + l2.val) + carry
            carry = 0
            if addy > 9:
                addy = addy % 10
                carry = 1
            
            head.val = addy
            if (l1.next != None and l2.next != None):
                head.next = ListNode()
                head = head.next
            l1 = l1.next
            l2 = l2.next

        if carry > 0:
            head.next = ListNode()
            head = head.next
            head.val = carry
        
        return real_head