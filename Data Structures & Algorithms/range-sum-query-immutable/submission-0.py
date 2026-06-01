class NumArray:
    def _initialize_pre_sum(self):
        for i, num in enumerate(self.nums):
            if i == 0:
                self.pre_sum.append(self.nums[i])
            else:
                self.pre_sum.append(self.pre_sum[i - 1] + self.nums[i])

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.pre_sum = []

        self._initialize_pre_sum()        

    def sumRange(self, left: int, right: int) -> int:
        return self.pre_sum[right] if left == 0 else self.pre_sum[right] - self.pre_sum[left - 1]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)