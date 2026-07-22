from collections import defaultdict

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        minimum = float("-inf")
        neighbors = defaultdict(list)

        for s, d, w in times:
            neighbors[s].append([d, w])
        
        shortest = {}
        min_heap = [[0, k]]
        while min_heap:
            w1, n1 = heapq.heappop(min_heap)
            
            if n1 in shortest:
                continue
            shortest[n1] = w1
            if w1 > minimum:
                minimum = w1
            
            for n2, w2 in neighbors[n1]:
                if n2 not in shortest:
                    heapq.heappush(min_heap, [w2 + w1, n2])
        
        return -1 if len(shortest) != n else minimum
