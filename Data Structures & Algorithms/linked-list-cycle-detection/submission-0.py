# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow_pointer = head
        fast_pointer = head

        while fast_pointer and fast_pointer.next:
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next

            if slow_pointer == fast_pointer:
                break
        
        if not fast_pointer or not fast_pointer.next:
            return False
        return True
        # slow_pointer_2 = head
        # while slow_pointer is not slow_pointer_2:
        #     slow_pointer_2 = slow_pointer_2.next
        #     slow_pointer = slow_pointer.next
 