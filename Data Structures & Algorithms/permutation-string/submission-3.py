from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        need = Counter(s1)
        L = 0
        for R in range(len(s2)):
            need[s2[R]] -= 1
            if R - L + 1 > n:
                need[s2[L]] += 1
                L += 1
            if R - L + 1 == n and all(v == 0 for v in need.values()):
                return True
        return False