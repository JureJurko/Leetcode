# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        ret_val = []
        i = 0
        while i < len(pairs):
            for j in range(i, 0, -1):
                if pairs[j].key < pairs[j - 1].key:
                    tmp = pairs[j]
                    pairs[j] = pairs[j - 1]
                    pairs[j - 1] = tmp
            
            ret_val.append(pairs[:])
            i += 1
        
        return ret_val