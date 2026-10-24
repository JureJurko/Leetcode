class Solution:
    def countSubstrings(self, s: str) -> int:
        T = "#" + "#".join(s) + "#"
        n = len(T)

        def extend(i):
            radius = 0
            while i - radius - 1 >= 0 and i + radius + 1 < n and T[i - radius - 1] == T[i + radius + 1]:
                radius += 1
            return radius
        
        P = [0] * n
        for i in range(n):
            P[i] = extend(i)
        return sum((p + 1) // 2 for p in P)

