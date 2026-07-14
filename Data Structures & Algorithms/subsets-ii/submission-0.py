class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        all_sets, curr_set = [], []
        nums.sort()
        self.helper(0, all_sets, curr_set, nums)

        return all_sets
    
    def helper(self, curr, all_sets, curr_set, nums):
        if curr >= len(nums):
            all_sets.append(curr_set.copy())
            return

        curr_set.append(nums[curr])
        self.helper(curr + 1, all_sets, curr_set, nums)
        curr_set.pop()

        while curr + 1 < len(nums) and nums[curr] == nums[curr + 1]:
            curr += 1
        self.helper(curr + 1, all_sets, curr_set, nums)
