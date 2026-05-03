import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_eating_speed = max(piles)
        min_eating_speed = 1

        result = max_eating_speed
        while min_eating_speed <= max_eating_speed:
            middle = (max_eating_speed + min_eating_speed) // 2

            summation = sum(math.ceil(x / middle) for x in piles)
            if summation > h:
                min_eating_speed = middle + 1
            if summation <= h:
                result = middle
                max_eating_speed = middle - 1
        
        return result








