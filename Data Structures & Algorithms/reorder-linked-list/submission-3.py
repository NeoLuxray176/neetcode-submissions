class Solution:
  def reorderList(self, head: Optional[ListNode]) -> None:
    # Find the middle (first half gets the extra node on even lengths)
    slow, fast = head, head
    while fast and fast.next:
      slow, fast = slow.next, fast.next.next

    # Split into two halves
    second = slow.next
    slow.next = None  # cut the first half loose

    # Reverse the second half; `prev` ends up as its new head
    prev, curr = None, second
    while curr:
      curr.next, prev, curr = prev, curr, curr.next

    # Interleave: first half in order, reversed second half woven in
    first, second = head, prev
    while second:
      first.next, second.next, first, second = second, first.next, first.next, second.next
