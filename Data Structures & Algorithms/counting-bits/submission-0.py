class Solution:
        def countBits(self, n: int) -> List[int]:
                res = []
                for  i  in  range(0,  n+1):
                        ones = 0
                        while i:
                                ones += i & 1
                                i = i >> 1
                    
                        res.append(ones)

                return res
                
