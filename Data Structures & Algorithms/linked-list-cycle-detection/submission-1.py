# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head.next

        while fast.next != None:
            if slow == fast:
                return True
            slow = slow.next
            fast = fast.next.next 
        
        return False