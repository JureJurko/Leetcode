# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def merge(self, pairs, s, m, e):
        left_pairs = pairs[s: m + 1]
        right_pairs = pairs[m + 1: e + 1]
        i, j, k = 0, 0, s

        while i < len(left_pairs) and j < len(right_pairs):
            if left_pairs[i].key <= right_pairs[j].key:
                pairs[k] = left_pairs[i]
                i += 1
            else:
                pairs[k] = right_pairs[j]
                j += 1
            k += 1
        
        while i < len(left_pairs):
            pairs[k] = left_pairs[i]
            i += 1
            k += 1
        while j < len(right_pairs):
            pairs[k] = right_pairs[j]
            j += 1
            k += 1

    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        return self.mergeSortHelper(pairs, 0, len(pairs) - 1)

    def mergeSortHelper(self, pairs: List[Pair], s: int, e: int) -> List[Pair]:

        if (e - s + 1 <= 1):
            return pairs
        
        mid_index = (s + e) // 2
        self.mergeSortHelper(pairs, s, mid_index)
        self.mergeSortHelper(pairs, mid_index+1, e)

        self.merge(pairs, s, mid_index, e)

        return pairs