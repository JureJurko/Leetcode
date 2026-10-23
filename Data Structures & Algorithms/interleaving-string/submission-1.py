class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        cache = [[-1] * (len(s1) + 1) for i in range(len(s2) + 1)]

        def dfs(p1, p2):
            if cache[p2][p1] != -1:
                return cache[p2][p1]
            
            if len(s1) == p1 and len(s2) == p2 and len(s3) == p1 + p2:
                cache[p2][p1] = True
                return True
            
            if p1 + p2 == len(s3):
                cache[p2][p1] = False
                return False
            
            if len(s1) > p1 and len(s2) > p2 and s1[p1] == s3[p1 + p2] and s2[p2] == s3[p1 + p2]:
                cache[p2][p1] = dfs(p1 + 1, p2) or dfs(p1, p2 + 1)
            elif len(s1) > p1 and s1[p1] == s3[p1 + p2]:
                cache[p2][p1] = dfs(p1 + 1, p2)
            elif len(s2) > p2 and s2[p2] == s3[p1 + p2]:
                cache[p2][p1] = dfs(p1, p2 + 1)
            else:
                cache[p2][p1] = False

            return cache[p2][p1]
            


        return dfs(0, 0)