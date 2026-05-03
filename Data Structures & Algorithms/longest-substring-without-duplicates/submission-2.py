class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        unique_chars = set()
        max_len = 0
        L = 0

        for R in range(len(s)):
            if s[R] not in unique_chars:
                unique_chars.add(s[R])
                max_len = max(max_len, R - L + 1)
            else:
                print("Novo")
                while s[L] != s[R]:
                    print(unique_chars)
                    print(s[L], s[R])
                    unique_chars.remove(s[L])
                    L += 1
                
                unique_chars.add(s[R])
                L+=1

                

        return max_len