from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d1 = defaultdict(list)
        d2 = defaultdict(int)

        for num in nums:
            if d2[num] > 0:
                d1[d2[num]].remove(num)
            d2[num] += 1
            d1[d2[num]].append(num)

        max_val = max(list(d2.values()))

        ret_val = []
        i = 0
        while i < k:
            val = d1[max_val]
            for v in val:
                if len(ret_val) == k:
                    return ret_val
                ret_val.append(v)
            
            i += len(val)
            max_val -= 1
        
        return ret_val



            
            
