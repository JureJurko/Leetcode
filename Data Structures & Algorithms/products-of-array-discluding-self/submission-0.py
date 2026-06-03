class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # l = [1, 1, 2, 8] r = [48, 24, 6, 1]
        # l[x] * r[x] ...

        total_product = 1
        l = []
        for num in nums:
            l.append(total_product)
            total_product *= num
        
        r = [0] * len(nums)
        total_product = 1
        for i, num in enumerate(nums[::-1]):
            r[len(nums) - 1 - i] = total_product
            total_product *= num
        
        return [x*y for x,y in zip(r, l)]



