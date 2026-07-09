class UnionFind:
    def __init__(self, n):
        self.rank = {}
        self.par = {}

        for i in range(1, n + 1):
            self.par[i] = i
            self.rank[i] = 0
        
    def _find(self, x):
        p = self.par[x]

        while p != self.par[p]:
            self.par[p] = self.par[self.par[p]]
            p = self.par[p]
        return p        
    
    def union(self, x, y):
        p_x = self._find(x)
        p_y = self._find(y)

        if p_x == p_y:
            return False
        
        if self.rank[p_x] > self.rank[p_y]:
            self.par[p_y] = p_x
        elif self.rank[p_x] < self.rank[p_y]:
            self.par[p_x] = p_y
        else:
            self.par[p_x] = p_y
            self.rank[p_y] += 1
        return True


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        unionFind = UnionFind(len(edges))

        for edge_x, edge_y in edges:
            if not unionFind.union(edge_x, edge_y):
                return [edge_x, edge_y]














        