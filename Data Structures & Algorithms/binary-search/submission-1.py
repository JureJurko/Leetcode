class Solution:
    def binary_search(self, nums: List[int], target: int, left, right) -> int:
        if left > right:
            return -1

        middle = (left + right) // 2
        if target > nums[middle]:
            return self.binary_search(nums, target, middle + 1, right)
        elif target < nums[middle]:
            return self.binary_search(nums, target, left, middle - 1)
        else:
            return middle
    
    def search(self, nums: List[int], target: int) -> int:
        return self.binary_search(nums, target, 0, len(nums) - 1)