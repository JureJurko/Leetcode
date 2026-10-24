class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)

        def expand(L, R):
            while L >= 0 and R < n and s[L] == s[R]:
                L -= 1
                R += 1
            return L + 1, R

        best_L, best_R = 0, 0
        for i in range(n):
            for L, R in (expand(i, i), expand(i, i + 1)):
                if R - L > best_R - best_L:
                    best_L, best_R = L, R

        return s[best_L:best_R]
