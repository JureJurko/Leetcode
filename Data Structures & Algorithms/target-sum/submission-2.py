class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        sum_max = sum(nums)
        table = [0] * (sum_max * 2 + 1)

        for i in range(len(table)):
            if i - sum_max == nums[0]:
                table[i] += 1
            if i - sum_max == -nums[0]:
                table[i] += 1

        curr_sum = nums[0]
        for i in range(1, len(nums)):
            curr_table = [0] * (sum_max * 2 + 1)
            for j in range(-curr_sum, curr_sum + 1):
                if table[sum_max + j] != 0:
                    curr_table[sum_max + j + nums[i]] = curr_table[sum_max + j + nums[i]] + table[sum_max + j]
                    curr_table[sum_max + j - nums[i]] = curr_table[sum_max + j - nums[i]] + table[sum_max + j]
            curr_sum += nums[i]
            table = curr_table
        
        index = sum_max + target
        if 0 <= index < len(table):
            return table[index]
        else:
            return 0




