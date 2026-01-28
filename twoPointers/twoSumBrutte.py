# Leet code problem no.167: Two sum problem
class Solution:
    def sum_of_pairs(self, nums, target):
        for i in range(len(nums) - 1):
            for j in range (i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return (i + 1, j + 1)

solution = Solution()
k = solution.sum_of_pairs([ 2, 9, 8, 5, 3, 4, 1 ], 10)
print(k)

"""
for i in range(len(nums) - 1):
    for j in range (i + 1, len(nums)):
The intitution behind this logic is to avoid duplicate pairs, to avoid addition of same element, to prevent last
element to find another pair.
"""
# Currently program has O(n^2) time and O(1) space complexity