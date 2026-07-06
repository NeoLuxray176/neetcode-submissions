# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        i = 1
        curr = head

        while curr:
            print(curr.val, i)
            if i == n:
                if curr.next:
                    curr.next = curr.next.next
                else:
                    if i == 1 and curr.next == None:
                        return None
                    else:
                        curr.next = None
                break
            curr = curr.next
            i += 1

        return head