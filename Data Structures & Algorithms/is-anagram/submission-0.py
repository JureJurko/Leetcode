from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        word_map = defaultdict(int)

        for char in s:
            word_map[char] += 1
        
        for char in t:
            if word_map[char] == 0:
                return False
            
            word_map[char] -= 1
        if any(list(word_map.values())) > 0:
            return False
        return True