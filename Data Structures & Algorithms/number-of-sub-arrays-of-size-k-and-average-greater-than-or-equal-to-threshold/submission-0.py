class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        L = 0 # [2,2,2,2,5,5,5,8]
        curr_sum = 0 # 0
        valid_subarrays = 0 # 0

        for R in range(len(arr)): # 1
            curr_sum += arr[R] # 6
            
            if R - L + 1 == k: # 3 == 3 
                valid_subarrays += 1 if curr_sum / k >= threshold else 0
                curr_sum -= arr[L]
                L += 1

        return valid_subarrays