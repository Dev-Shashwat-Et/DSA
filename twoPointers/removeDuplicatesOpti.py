# Remove duplicates in sorted array or list 

class Solution:
    def removeDuplicates(self,nums):

        if not nums:
            return 0 

        left = 0
        for right in range(1,len(nums)):
            if nums[left] != nums[right]:
                left += 1
                nums[left] = nums[right] # Modifies nums

        return left + 1
   
solution = Solution()
nums = [1,1,2,3,3,5] 

k = solution.removeDuplicates(nums)
print(nums[:k])



        
        
