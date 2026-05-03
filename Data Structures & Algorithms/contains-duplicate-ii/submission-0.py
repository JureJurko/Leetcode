class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        L = 0
        visited = set()

        for R in range (len(nums)):
            if R - L - 1 >= k:
                visited.remove(nums[L])
                L += 1
            if nums[R] in visited:
                return True
            else:
                visited.add(nums[R])

        return False