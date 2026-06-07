class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Solution using O(N) extra space
        hash_map = {}
        
        for num in nums:
            if num in hash_map:  
                return num

            hash_map[num] = True
