class DSU:
    def __init__(self, n: int):
        self.par = list(range(n))
        self.rank = [0] * n
    
    def find(self, n: int) -> int:
        if n != self.par[n]:
            self.par[n] = self.find(self.par[n])
        return self.par[n]
    
    def union(self, n1: int, n2: int) -> bool:
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
        edges.sort(key=lambda edge: edge[2])
        
        dsu = DSU(n)
        mst_weight = 0
        edges_used = 0

        for u, v, w in edges:
            if dsu.union(u, v):
                mst_weight += w
                edges_used += 1
                
                if edges_used == n - 1:
                    return mst_weight
        
        return mst_weight if edges_used == n - 1 else -1