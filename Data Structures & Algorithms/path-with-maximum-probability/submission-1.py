from collections import defaultdict


class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        neighbors = defaultdict(list)

        for edge, probability in zip(edges, succProb):
            s, d = edge
            neighbors[s].append([d, probability])
            neighbors[d].append([s, probability])
        
        max_heap = [[1, start_node]]
        shortest = {}

        while max_heap:
            w1, n1 = heapq.heappop_max(max_heap)
            if n1 in shortest:
                continue
            
            shortest[n1] = w1

            if end_node in shortest:
                return shortest[end_node]

            for n2, w2 in neighbors[n1]:
                if n2 not in shortest:
                    heapq.heappush_max(max_heap, [w1 * w2, n2])
        print(shortest)
        return 0
