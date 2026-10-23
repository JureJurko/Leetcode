class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        dp = [1 for i in range(m + 1)]

        for i in range(n):
            new_dp = [0 for i in range(m + 1)]
            for j in range(m):
                if s[j] == t[i]:
                    new_dp[j + 1] = new_dp[j] + dp[j]
                else:
                    new_dp[j + 1] = new_dp[j]
            dp = new_dp[:]
        
        return dp[m]




