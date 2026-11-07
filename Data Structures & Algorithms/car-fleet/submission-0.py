class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        times = [None] * target
        for p, s in zip(position, speed):
            times[p] = (target - p) / s

        fleets = 0
        slowest = 0
        for t in reversed(times):
            if t is not None and t > slowest:
                fleets += 1
                slowest = t
        return fleets