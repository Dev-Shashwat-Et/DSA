# Leet code problem no.167: Two sum problem
class Solution:
    def sum_of_pairs(self, nums):
        for num in nums:
            if num == 3:
                return num


solution = Solution()
nums = [ 2, 9, 8, 5, 3, 4, 1 ]
k = solution.sum_of_pairs(nums)
print(k)