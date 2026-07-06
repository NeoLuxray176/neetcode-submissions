# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = newList = ListNode()

        head1 = list1
        head2 = list2

        while head1 != None and head2 != None:
            if head1.val < head2.val:
                newList.next = head1
                head1 = head1.next
            else:
                newList.next = head2
                head2 = head2.next
            newList = newList.next

        while head1 != None:
            newList.next = head1
            head1 = head1.next
            newList = newList.next

        while head2 != None:
            newList.next = head2
            head2 = head2.next
            newList = newList.next

        return dummy.next