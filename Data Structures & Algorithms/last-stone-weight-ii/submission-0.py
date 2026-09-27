import copy
from math import ceil
class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        stoneSum = sum(stones)
        target = ceil(stoneSum / 2)

        def dfs(i, total):
            if total >= target or i == len(stones):
                return abs(total - (stoneSum - total))
            if (i, total) in cache:
                return cache[(i, total)]
            
            cache[(i, total)] = min(
                dfs(i + 1, total),
                dfs(i + 1, total + stones[i])
            )
            
            return cache[(i, total)]
        
        cache = {}
        return dfs(0, 0)




