class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        results = []
        nums.sort()


        for i, num in enumerate(nums):
            if i > 0 and num == nums[i - 1]:
                continue
            L, R = i + 1, len(nums) - 1
            while L < R:
                curr_sum = num + nums[L] + nums[R]
                if curr_sum > 0:
                    R -= 1
                elif curr_sum < 0:
                    L += 1
                else:
                    results.append([num, nums[L], nums[R]])
                    L += 1
                    while nums[L] == nums[L-1] and L < R:
                        L += 1
        return results
