class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # 1. Find the middle
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 2. Cut, then reverse the second half
        second = slow.next
        slow.next = None
        prev = None
        while second:
            nxt = second.next
            second.next = prev
            prev = second
            second = nxt

        # 3. Merge: your original loop, unchanged
        merge_head = head
        merge_curr = prev
        while merge_curr and merge_head:
            merge_head_next = merge_head.next
            merge_curr_next = merge_curr.next
            merge_head.next = merge_curr
            merge_curr.next = merge_head_next

            merge_head = merge_head_next
            merge_curr = merge_curr_next