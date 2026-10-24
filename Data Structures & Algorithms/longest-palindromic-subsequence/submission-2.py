from functools import cache
import sys
sys.setrecursionlimit(2000)
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        max_len = 0
        @cache
        def backtrack(p1, p2):
            if p1 == p2:
                return 1
            if p1 >= len(s) or p2 < 0 or p1 > p2:
                return 0
            if s[p1] == s[p2]:
                max_len = 2 + backtrack(p1 + 1, p2 - 1)
            else:
                max_len = max(
                    backtrack(p1 + 1, p2),
                    backtrack(p1, p2 - 1)
                )

            return max_len
        
        return backtrack(0, len(s) - 1)