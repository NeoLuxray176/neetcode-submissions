# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        curr = head
        group = 0
        while curr and group < k:
            curr = curr.next
            group += 1

        if group == k:
            curr = self.reverseKGroup(curr, k)
            while 0 < group:
                tmp = head.next
                head.next = curr
                curr = head
                head = tmp
                group -= 1
            head = curr
        return head