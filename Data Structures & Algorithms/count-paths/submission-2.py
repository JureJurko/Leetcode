class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        def dfs(curr_m, curr_n):
            if curr_m == m or curr_n == n:
                return 0
            if curr_m == m-1 and curr_n == n-1:
                return 1
            
            return dfs(curr_m+1, curr_n) + dfs(curr_m, curr_n+1)
        
        return dfs(0, 0)