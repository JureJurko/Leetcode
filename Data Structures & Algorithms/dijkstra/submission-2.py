from collections import defaultdict


class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        neighbors = defaultdict(list)
        for s, d, w in edges:
            neighbors[s].append([d, w])
        


        min_heap = [[0, src]]
        shortest = {}
        while min_heap:
            w1, n1 = heapq.heappop(min_heap)
            if n1 in shortest:
                continue
            shortest[n1] = w1

            for n2, w2 in neighbors[n1]:
                if n2 not in shortest:
                    heapq.heappush(min_heap,  [w2 + w1, n2])
        
        for i in range(n):
            if i not in shortest:
                shortest[i] = -1

        return shortest


