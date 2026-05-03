class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxArray = nums[0]
        curr = 0

        for num in nums:
            curr = max(curr, 0)
            curr += num
            maxArray = max(maxArray, curr)
        
        return maxArray