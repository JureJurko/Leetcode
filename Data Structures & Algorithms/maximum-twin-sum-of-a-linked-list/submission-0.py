# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow = fast = head
        hash_map = {}
        counter = 0

        while fast and fast.next:
            hash_map[counter] = slow.val
            counter = counter + 1
            slow = slow.next
            fast = fast.next.next
        
        max_twin_sum = None
        n = counter * 2
        while slow:
            curr_twin_sum = hash_map[n - 1 - counter] + slow.val
            if max_twin_sum is None or max_twin_sum < curr_twin_sum:
                max_twin_sum = curr_twin_sum
            slow = slow.next
            counter = counter + 1

        return max_twin_sum
            

        

        