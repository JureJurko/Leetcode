class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]

        for num in nums:
            for subset in list(result):
                new_subset = subset + [num]
                result.append(new_subset)

        return result

            

            

