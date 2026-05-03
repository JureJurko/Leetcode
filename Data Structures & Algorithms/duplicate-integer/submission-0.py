class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_dict = {}

        for num in nums:
            if num not in nums_dict:
                nums_dict[num] = True
            else:
                return nums_dict[num]
        
        return False