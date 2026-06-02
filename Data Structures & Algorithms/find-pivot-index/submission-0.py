class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left_sum = 0
        right_sum = 0
        pivot = 0

        for i in range(len(nums)):
            pivot = i
            left_sum = sum(nums[:i:])
            right_sum = sum(nums[i+1:len(nums):])

            if left_sum == right_sum:
                return i
        
        return -1