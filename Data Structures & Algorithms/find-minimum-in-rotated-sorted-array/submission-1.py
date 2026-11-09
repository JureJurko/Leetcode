class Solution:
    def findMin(self, nums: List[int]) -> int:
        L, R, M = 0, len(nums) - 1, 0

        while L != R:
            M = (L + R) // 2
            if nums[M] > nums[R]:
                if M == L:
                    L = M + 1
                else:
                    L = M
            elif nums[M] < nums[R]:
                R = M
        
        return nums[(L + R) // 2]