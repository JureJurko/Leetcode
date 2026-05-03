class Solution:
    def sortColors(self, nums: List[int]) -> None:
        counters = [0, 0, 0]
        for num in nums:
            counters[num] += 1
        
        i = 0
        for n in range(len(counters)):
            for j in range(counters[n]):
                nums[i] = n
                i += 1
        