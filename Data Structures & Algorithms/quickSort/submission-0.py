# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        return self.helper_quickSort(pairs, 0, len(pairs) - 1)
    
    def helper_quickSort(self, pairs, s, e):
        print(f"{s=}...{e=}")
        if e - s <= 0:
            return pairs
        
        pivot = pairs[e]
        j = 0
        for i in range(e - s):
            if pairs[i + s].key < pivot.key:
                tmp = pairs[s + j]
                pairs[s + j] = pairs[i + s]
                pairs[i + s] = tmp
                j += 1

        tmp = pairs[s + j]
        pairs[s + j] = pivot
        pairs[e] = tmp

        self.helper_quickSort(pairs, s, s + j - 1)
        self.helper_quickSort(pairs, s + j + 1, e)

        return pairs

            
