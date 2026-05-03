class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq_map = {}
        max_len = 0
        L = 0

        for R in range(len(s)):
            if s[R] not in freq_map:
                freq_map[s[R]] = 1
            else:
                freq_map[s[R]] += 1
            
            while R - L + 1 - max(freq_map.values()) > k:
                freq_map[s[L]] -= 1
                L += 1
            
            max_len = max(max_len, R - L + 1)

        return max_len


