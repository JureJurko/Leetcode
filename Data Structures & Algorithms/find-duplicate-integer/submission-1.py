class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # [2, 1, 2, 4, 3]
        # Use slow + fast pointer and jumping by positions, not next
        slow = fast = nums[0]

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break
        
        new_slow = nums[0]
        while slow != new_slow:
            slow = nums[slow]
            new_slow = nums[new_slow]
        
        return slow