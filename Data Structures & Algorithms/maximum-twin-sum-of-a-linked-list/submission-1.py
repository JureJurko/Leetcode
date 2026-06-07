class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow = fast = head
        first_half = []

        while fast and fast.next:
            first_half.append(slow.val)
            slow = slow.next
            fast = fast.next.next
        
        max_twin_sum = 0
        
        while slow:
            curr_twin_sum = first_half.pop() + slow.val
            max_twin_sum = max(max_twin_sum, curr_twin_sum)
            slow = slow.next

        return max_twin_sum