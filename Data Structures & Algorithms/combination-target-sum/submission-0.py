class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = list()
        
        self.current = list()
        self.current_sum = 0
        def backtrack(index):
            if self.current_sum == target:
                result.append(self.current.copy())
                return
            if index >= len(nums) or self.current_sum > target:
                return
            
            self.current.append(nums[index])
            self.current_sum += nums[index]
            backtrack(index)

            val = self.current.pop()
            self.current_sum -= val
            backtrack(index + 1)


        backtrack(0)
        return result
