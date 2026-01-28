# Leet code problem: 167
class Solution:
    def sum_of_pairs(self, nums, target):
        left, right = 0, len(nums)-1

        while left < right: 
            current_sum = nums[left] + nums[right]

            if current_sum == target:
                return (left + 1, right + 1)
            elif current_sum < target:
                    left += 1
            else:
                right -= 1
        return None # It just for good practice as python by default returns none if no pair is found


solution = Solution()
print(solution.sum_of_pairs([0,4,5,7,9,16], 12))
print(solution.sum_of_pairs([0,4,5,7,9,16], 50))


"""
You can also use this approach but it is not so cleaner version
        while left < right: 
            if nums[left] + nums[right] == target:
                return (left + 1, right + 1)
            elif nums[left] + nums[right] < target:
                    left += 1
            else:
                right -= 1
        return None  

"""
# Time complexity: O(n)
# Space complexit: O(1)