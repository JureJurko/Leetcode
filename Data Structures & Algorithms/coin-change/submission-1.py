class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        lista coins je zapravo weight u normalnom knapsack problemu,
        a amount je kapacitet i s obzirom da nema profita, ne bilježimo profit
        već koliko novičića treba prije nego što prekoračimo zadani kapacitet.
        U dp listi ćemo imati tuple[int, int] gdje je prva vrijednost težina koju smo dosegli,
        a druga vrijednost broj novčića korištenih da se to dosegne 
        """
        dp = [(0, 0)] * (amount + 1)

        for i in range(0, len(coins)):
            new_dp = [(0, 0)] * (amount + 1)
            for c in range(1, amount + 1):
                skip = dp[c]
                include = (0, 0)

                if c - coins[i] >= 0:
                    include = (coins[i] + new_dp[c - coins[i]][0], new_dp[c - coins[i]][1] + 1)
                
                new_dp[c] = max(skip, include, key=lambda x: (x[0], -x[1]))
            dp = new_dp
        
        return dp[-1][1] if dp[-1][0] == amount else -1
                




