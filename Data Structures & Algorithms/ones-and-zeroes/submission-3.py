class Solution:
    def findMaxForm(self, strs: List[str], M: int, N: int) -> int:
        cache = defaultdict(int)

        for s in strs:
            count_m, count_n = s.count("0"), s.count("1")
            for m in range(M, count_m - 1, -1):
                for n in range(N, count_n - 1, -1):
                    cache[(m, n)] = max(
                        1 + cache[(m - count_m, n - count_n)],
                        cache[(m, n)]
                    )
        
        return cache[(M, N)]
