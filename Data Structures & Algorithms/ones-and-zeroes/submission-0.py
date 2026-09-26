class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        #Memoization
        cache = {}

        def dfs(i, m, n):
            if i == len(strs):
                return 0
            if (i, m, n) in cache:
                return cache[(i, m, n)]
            
            count_m, count_n = strs[i].count("0"), strs[i].count("1")
            cache[(i, m, n)] = dfs(i + 1, m, n)
            if count_m <= m and count_n <= n:
                cache[(i, m, n)] = max(
                    cache[(i, m, n)],
                    1 + dfs(i + 1, m - count_m, n - count_n) 
                )
            return cache[(i, m, n)]
        
        return dfs(0, m, n)
