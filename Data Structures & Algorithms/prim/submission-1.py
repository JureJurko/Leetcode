from collections import defaultdict


class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)

        for n1, n2, weight in edges:
            adj[n1].append([n2, weight])
            adj[n2].append([n1, weight])
    

        min_heap = []
        for neighbor, weight in adj[0]:
            heapq.heappush(min_heap, [weight, 0, neighbor])

        mst = 0
        visit = set()
        visit.add(0)
        while len(visit) < n:
            if not min_heap:
                return -1
            weight, n1, n2 = heapq.heappop(min_heap)
            if n2 in visit:
                continue
            
            mst += weight
            visit.add(n2)
            for neighbor, weight in adj[n2]:
                if neighbor not in visit:
                    heapq.heappush(min_heap, [weight, n2, neighbor])
        
        return mst

