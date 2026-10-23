from functools import cache

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        return self.dfs(s, t, 0, 0)

    @cache
    def dfs(self, s, t, p1, p2):
        if p2 == len(t):
            return 1
        if p1 == len(s):
            return 0

        if s[p1] == t[p2]:
            return self.dfs(s, t, p1 + 1, p2 + 1) + self.dfs(s, t, p1 + 1, p2)
        else:
            return self.dfs(s, t, p1 + 1, p2)

