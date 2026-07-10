class DSU:
    def __init__(self, n):
        self.rank = {}
        self.par = {}
        self.num_of_components = n

        for i in range(n):
            self.par[i] = i
            self.rank[i] = 0

    def find(self, x):
        p = self.par[x]
        while p != self.par[p]:
            self.par[p] = self.par[self.par[p]]
            p = self.par[p]
        return p


    def union(self, x, y):
        p_x = self.find(x)
        p_y = self.find(y)

        if p_x == p_y:
            return False
        
        if self.rank[p_x] > self.rank[p_y]:
            self.par[p_y] = p_x
        elif self.rank[p_x] < self.rank[p_y]:
            self.par[p_x] = p_y
        else:
            self.par[p_x] = p_y
            self.rank[p_y] += 1
        
        self.num_of_components -= 1
        return True


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        dsu = DSU(n)

        for edge_x, edge_y in edges:
            dsu.union(edge_x, edge_y)
        
        return dsu.num_of_components
        