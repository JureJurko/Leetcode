from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        L, R = 0, 0
        ct = Counter(s1)
        if ct.get(s2[L]) is not None:
            ct[s2[L]] = ct[s2[L]] - 1
        if ct.most_common()[0][1] == 0:
                return True
        while R < len(s2) - 1:
            if R - L >= n - 1:
                if ct.get(s2[L]) is not None:
                    ct[s2[L]] = ct[s2[L]] + 1
                L += 1

            R += 1
            if ct.get(s2[R]) is not None:
                 ct[s2[R]] = ct[s2[R]] - 1
            if ct.most_common()[0][1] == 0:
                return True

        return False
            



        