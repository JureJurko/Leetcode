class Solution:
    def longestPalindrome(self, s: str) -> str:
        T = "#" + "#".join(s) + "#"
        n = len(T)

        def expand(i):
            r = 0
            while i - r - 1 >= 0 and i + r + 1 < n and T[i - r - 1] == T[i + r + 1]:
                r += 1
            return r

        P = [0] * n
        for i in range(n):
            P[i] = expand(i)

        center = max(range(n), key=lambda k: P[k])
        start = (center - P[center]) // 2
        return s[start:start + P[center]]