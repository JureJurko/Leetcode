# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        curr = head
        list_len = 0
        while curr:
            list_len += 1
            curr = curr.next

        del_position = list_len - n

        curr = head
        prev = None
        while del_position > 0:
            prev = curr
            curr = curr.next
            del_position -= 1
        
        if prev is None:
            return curr.next
        
        tmp = curr.next
        prev.next = tmp
        return head
