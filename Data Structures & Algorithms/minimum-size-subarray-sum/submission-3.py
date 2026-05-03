class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        L = 0
        length = 0
        curr_sum = 0

        for R in range(len(nums)):
            curr_sum += nums[R]

            if (curr_sum >= target and R - L + 1 < length) or (length == 0 and curr_sum >= target):
                length = R - L + 1

            while curr_sum > target:
                curr_sum -= nums[L]
                L += 1
                if curr_sum >= target and R - L + 1 < length:
                    length = R - L + 1
            
        return length