class Solution:
    def longestPalindrome(self, s: str) -> str:
        L_odd, R_odd, L_even, R_even = 0, 0, 0, 0
        length = 0
        for i in range(len(s)):
            L, R = i, i
            while L >= 0 and R < len(s) and s[L] == s[R]:
                if (R - L + 1) > length:
                    length = R - L + 1
                    L_odd = L
                    R_odd = R
                L -= 1
                R += 1
            
            L, R = i, i + 1
            while L >= 0 and R < len(s) and s[L] == s[R]:
                if (R - L + 1) > length:
                    length = R - L + 1
                    L_even = L
                    R_even = R
                L -= 1
                R += 1
            
        return max(s[L_odd:R_odd + 1], s[L_even:R_even + 1], key=len)
