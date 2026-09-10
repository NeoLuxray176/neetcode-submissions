class Solution:
    def reverse_list(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head

        while curr:
            curr.next, curr, prev = prev, curr.next, curr

        return prev

    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        # Find the end of the first half.
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # Split the list into two independent lists.
        second = slow.next
        slow.next = None

        # Reverse only the second half.
        second = self.reverse_list(second)

        # Alternate between the first and reversed second half.
        first = head

        while second:
            first_next = first.next
            second_next = second.next

            first.next = second
            second.next = first_next

            first = first_next
            second = second_next