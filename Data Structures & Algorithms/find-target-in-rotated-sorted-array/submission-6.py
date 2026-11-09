class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L, R = 0, len(nums) - 1

        while L <= R:
            M = (L + R) // 2
            print(nums[L], nums[M], nums[R])
            if nums[M] == target:
                return M
            elif target >= nums[L] > nums[M] or nums[M] > target >= nums[L] or nums[L] > nums[M] > target:
                R = M
            else:
                L = M + 1
        
        return -1