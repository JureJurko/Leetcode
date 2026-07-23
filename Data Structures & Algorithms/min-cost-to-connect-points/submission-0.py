from collections import defaultdict

class Solution:
    @staticmethod
    def calculate_distance(p1, p2):
        x1, y1 = p1
        x2, y2 = p2
        return abs(x2 - x1) + abs(y2 - y1)

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj = defaultdict(list)

        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                p1 = points[i]
                p2 = points[j]
                dst = Solution.calculate_distance(p1, p2)
                adj[tuple(p1)].append([p2, dst])
                adj[tuple(p2)].append([p1, dst])
        
        mst = 0
        visit = set()
        min_heap = []

        starting_point = tuple(points[0])

        for point, dst in adj[starting_point]:
            heapq.heappush(min_heap, [dst, point])
        
        visit.add(starting_point)

        while min_heap and len(visit) < len(points):
            w1, p1 = heapq.heappop(min_heap)
            if tuple(p1) in visit:
                continue
            
            mst += w1
            visit.add(tuple(p1))

            for p2, w2 in adj[tuple(p1)]:
                if tuple(p2) not in visit:
                    heapq.heappush(min_heap, [w2, p2])
        
        return mst




















        