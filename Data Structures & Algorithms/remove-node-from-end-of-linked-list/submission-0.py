# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        i = 0
        curr = head

        while head.next != None and i < n:
            curr = head.next
            i += 1
        
        if curr.next != None:
            curr.next = curr.next.next
        else:
            return head.next

        return head