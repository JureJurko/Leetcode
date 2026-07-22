class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        permutations = set()
        permutations.add((nums[0],))

        for n in nums[1:]:
            next_permutations = set()
            for permutation in permutations:
                for position in range(len(permutation) + 1):
                    copy_of_permutation = list(permutation)
                    copy_of_permutation.insert(position, n)
                    next_permutations.add(tuple(copy_of_permutation))
            permutations = next_permutations

        return list(permutations)
