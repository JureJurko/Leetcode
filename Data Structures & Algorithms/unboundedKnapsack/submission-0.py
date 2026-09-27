class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        col, rows = len(profit), capacity
        dp = [0] * (rows + 1)

        for i in range(0, col):
            new_dp = [0] * (rows + 1)
            for c in range(1, capacity + 1):
                skip = dp[c]
                include = 0

                if c - weight[i] >= 0:
                    include = profit[i] + new_dp[c - weight[i]]
                
                new_dp[c] = max(skip, include)
            dp = new_dp

        return dp[-1]