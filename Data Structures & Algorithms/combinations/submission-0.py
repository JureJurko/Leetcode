class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        combinations = []
        curr_comb = []
        self.helper(1, combinations, curr_comb, n, k)
        return combinations
    
    def helper(self, i, combinations, curr_comb, n, k):
        if len(curr_comb) == k:
            combinations.append(curr_comb.copy())
            return
        if i > n:
            return
        
        for j in range(i, n + 1):
            curr_comb.append(j)
            self.helper(j + 1, combinations, curr_comb, n, k)
            curr_comb.pop()
        
        return
