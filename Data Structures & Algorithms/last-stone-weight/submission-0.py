import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = stones

        heapq.heapify_max(stones) # Create a minHeap

        while len(stones) > 1:
            largest = heapq.heappop_max(stones)
            second_largest = heapq.heappop_max(stones)
            if largest > second_largest:
                heapq.heappush_max(stones, largest - second_largest)
        
        return 0 if not stones else stones[0]


