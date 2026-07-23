class DSU:
    def __init__(self, n):
        self.par = {
            i : i
            for i in range(n)
        }

        self.rank = {
            i : 0
            for i in range(n)
        }
    
    def find(self, n):
        if n != self.par[n]:
            self.par[n] = self.find(self.par[n])
        return self.par[n]
    
    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)

        if p1 == p2:
            return False
        
        if self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1
        elif self.rank[p1] < self.rank[p2]:
            self.par[p1] = p2
        else:
            self.par[p1] = p2
            self.rank[p2] += 1
        return True


class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        min_heap = []

        for s, d, w in edges:
            heapq.heappush(min_heap, [w, s, d])
        
        mst = 0
        dsu = DSU(n)
        counter = 0

        while min_heap and counter < n - 1:
            w, s, d = heapq.heappop(min_heap)
            if not dsu.union(s, d):
                continue
            
            mst += w
            counter += 1
        
        return mst if counter == n - 1 else -1

















