import heapq

class MedianFinder:
    def __init__(self):
        self.small, self.big = [], [] # max-heap, min-heap

    def addNum(self, num: int) -> None:
        heapq.heappush_max(self.small, num)
        if (self.small
            and self.big
            and self.small[0] > self.big[0]):
            pop_val = heapq.heappop_max(self.small)
            heapq.heappush(self.big, pop_val)
        
        if len(self.small) - 1 > len(self.big):
            pop_val = heapq.heappop_max(self.small)
            heapq.heappush(self.big, pop_val)
        if len(self.small) + 1 < len(self.big):
            pop_val = heapq.heappop(self.big)
            heapq.heappush_max(self.small, pop_val)

    def findMedian(self) -> float:
        if len(self.small) > len(self.big):
            return self.small[0]
        elif len(self.small) < len(self.big):
            return self.big[0]
        
        return (self.big[0] + self.small[0]) / 2
        
        