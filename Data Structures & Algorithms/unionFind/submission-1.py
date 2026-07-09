class UnionFind:
    def __init__(self, n: int):
        self.num_of_components = n
        self.par = {}
        self.rank = {}

        for i in range(n):
            self.par[i] = i
            self.rank[i] = 0

    def find(self, x: int) -> int:
        p = self.par[x]

        while p != self.par[p]:
            self.par[p] = self.par[self.par[p]]
            p = self.par[p]
        return p

    def isSameComponent(self, x: int, y: int) -> bool:
        p_x = self.find(x)
        p_y = self.find(y)

        return p_x == p_y

    def union(self, x: int, y: int) -> bool:
        if self.isSameComponent(x, y):
            return False

        p_x = self.find(x)
        p_y = self.find(y)

        if self.rank[p_x] > self.rank[p_y]:
            self.par[p_y] = p_x
        elif self.rank[p_x] < self.rank[p_y]:
            self.par[p_x] = p_y
        else:
            self.par[p_x] = p_y
            self.rank[p_y] += 1
        
        self.num_of_components -= 1
        return True

    def getNumComponents(self) -> int:
        return self.num_of_components
