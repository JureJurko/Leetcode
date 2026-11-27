class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res, cur = [], []
        candidates.sort()
        def combinate(cur_sum, i):
            if cur_sum == target:
                res.append(cur.copy())
                return

            if i == len(candidates) or cur_sum > target:
                return
            
            cur.append(candidates[i])
            combinate(cur_sum + candidates[i], i + 1)
            cur.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            combinate(cur_sum, i + 1)
        
        combinate(0, 0)
        return res
         
