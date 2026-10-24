from functools import cache
import sys
sys.setrecursionlimit(10000)
class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        @cache
        def backtrack(p1, p2):
            if p1 >= len(str1):
                return len(str2) - p2
            elif p2 >= len(str2):
                return len(str1) - p1
            
            char_1 = str1[p1]
            char_2 = str2[p2]
            if char_1 == char_2:
                return 1 + backtrack(p1 + 1, p2 + 1)
            else:
                return min(
                    1 + backtrack(p1 + 1, p2),
                    1 + backtrack(p1, p2 + 1),
                )

        backtrack(0, 0)
        result = ""
        p1, p2 = 0, 0
        while p1 < len(str1) or p2 < len(str2):
            if p1 >= len(str1):
                return result + str2[p2:]
            if p2 >= len(str2):
                return result + str1[p1:]
            
            if str1[p1] == str2[p2]:
                result += str1[p1]
                p1 += 1
                p2 += 1
            else:
                if backtrack(p1 + 1, p2) < backtrack(p1, p2 + 1):
                    result += str1[p1]
                    p1 += 1
                else:
                    result += str2[p2]
                    p2 += 1

        return result 








