from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)
        missing = len(t)
        best_L, best_len = 0, float("inf")
        L = 0
        for R, c in enumerate(s):
            if need[c] > 0:
                missing -= 1
            need[c] -= 1
            while missing == 0:
                if R - L + 1 < best_len:
                    best_L, best_len = L, R - L + 1
                need[s[L]] += 1
                if need[s[L]] > 0:             # dropped a needed character
                    missing += 1
                L += 1
        return "" if best_len == float("inf") else s[best_L:best_L + best_len]