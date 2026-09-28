class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [(0, 0)] * (amount + 1)
        if amount == 0:
            return 1
        for c in coins:
            new_dp = [(0, 0)] * (amount + 1)
            for a in range(1, amount + 1):
                skip = dp[a]
                include = (0, 0)
                if a - c > 0:
                    include = (c + new_dp[a - c][0], new_dp[a - c][1] + skip[1])
                elif a - c == 0:
                    include = (c + new_dp[a - c][0], new_dp[a - c][1] + 1 + skip[1])
                        
                
                new_dp[a] = max(skip, include)
            dp = new_dp
        
        return dp[amount][1] if dp[amount][0] == amount else 0



