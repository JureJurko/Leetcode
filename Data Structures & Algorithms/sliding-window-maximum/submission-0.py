from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        res = []
        for R in range(len(nums)):
            while q and nums[q[-1]] < nums[R]:
                q.pop()
            q.append(R)
            if q[0] <= R - k:
                q.popleft()
            if R >= k - 1:
                res.append(nums[q[0]])
        return res