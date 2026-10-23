class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        cache = [[-1 for j in range(len(t))] for m in range(len(s))]
        return self.dfs(s, t, 0, 0, cache)

    def dfs(self, s, t, p1, p2, cache):
        if p2 == len(t):
            return 1
        if p1 == len(s):
            return 0
        if cache[p1][p2] != -1:
            return cache[p1][p2]

        if s[p1] == t[p2]:
            cache[p1][p2] = self.dfs(s, t, p1 + 1, p2 + 1, cache) + self.dfs(s, t, p1 + 1, p2, cache)
        else:
            cache[p1][p2] = self.dfs(s, t, p1 + 1, p2, cache)
        
        return cache[p1][p2]


