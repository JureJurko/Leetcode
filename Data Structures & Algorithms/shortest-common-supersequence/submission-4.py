from functools import cache
import sys
sys.setrecursionlimit(2000)
class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        n, m = len(str1), len(str2)
        @cache
        def scs_len(i, j):
            if i == n:
                return m - j
            if j == m:
                return n - i
            if str1[i] == str2[j]:
                return 1 + scs_len(i + 1, j + 1)
            return 1 + min(scs_len(i + 1, j), scs_len(i, j + 1))

        out = []
        i = j = 0
        while i < n and j < m:
            if str1[i] == str2[j]:
                out.append(str1[i])
                i += 1
                j += 1
            elif scs_len(i + 1, j) < scs_len(i, j + 1):
                out.append(str1[i])
                i += 1
            else:
                out.append(str2[j])
                j += 1
        out.append(str1[i:])
        out.append(str2[j:])
        return "".join(out)

        return result 








