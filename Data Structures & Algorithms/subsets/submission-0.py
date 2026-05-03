class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ret_val = list()
        n = len(nums)
        configs = [f'{i:0{n}b}' for i in range(2**n)] # O(2^n)
        
        for config in configs: # O(2^n)
            ret_val.append([j for i, j in enumerate(nums) if config[i] == "1"]) # (O(n))
        
        return ret_val

            

            

            

