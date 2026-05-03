class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}

        for i, num in enumerate(nums):
            if num in nums_dict:
                return [nums_dict[num], i]
            
            nums_dict[target - num] = i