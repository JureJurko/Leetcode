import copy
from math import ceil
class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        stoneSum = sum(stones)
        target = stoneSum // 2
        cache = {0}

        for stone in stones:
            new_cache = set(cache)
            for val in cache:
                if val + stone == target:
                    return stoneSum - 2 * target
                if val + stone < target:
                    new_cache.add(val + stone)
            cache = new_cache
        
        return stoneSum - 2 * max(cache)
        




