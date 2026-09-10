class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        dummy = Node(x=-1)
        new_curr = dummy
        curr = head

        d = {}

        # First pass: copy nodes and next pointers
        while curr:
            new_curr.next = Node(x=curr.val)
            new_curr = new_curr.next

            d[curr] = new_curr
            curr = curr.next

        # Second pass: copy random pointers
        curr = head
        new_curr = dummy.next

        while curr:
            if curr.random:
                new_curr.random = d[curr.random]

            curr = curr.next
            new_curr = new_curr.next

        return dummy.next