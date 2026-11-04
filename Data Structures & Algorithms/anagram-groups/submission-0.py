from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dicts = defaultdict(list)
        
        for string in strs:
            d = [0] * 26
            for char in string:
                d[ord(char) - ord('a')] += 1

            dicts[tuple(d)].append(string)
        
        return list(dicts.values())

            