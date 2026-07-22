class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = [[]]

        for n in nums:
            next_permutations = []
            for p in permutations:
                for position in range(len(p) + 1):
                    copy_of_permutation = p.copy()
                    copy_of_permutation.insert(position, n)
                    next_permutations.append(copy_of_permutation)
            permutations = next_permutations
        
        return permutations