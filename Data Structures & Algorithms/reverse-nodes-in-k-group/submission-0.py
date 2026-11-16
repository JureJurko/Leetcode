class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        group_prev = dummy

        while True:
            # 1. Find the k-th node; stop if the group is too short
            kth = group_prev
            for _ in range(k):
                kth = kth.next
                if kth is None:
                    return dummy.next
            group_next = kth.next

            # 2. Reverse the group; its first node ends up pointing to group_next
            prev, curr = group_next, group_prev.next
            while curr is not group_next:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt

            # 3. Reconnect: the old first node is now the group's last node
            old_first = group_prev.next
            group_prev.next = kth
            group_prev = old_first