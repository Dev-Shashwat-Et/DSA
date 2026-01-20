# Leetcode - No.26  Remove duplicates in sorted array or list 

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

"""
# Using while loop but 
def removeDuplicates(nums):
    if not nums:
        return 0
    
    left = 0
    right = 1  # We have to initialize manually
    
    while right < len(nums):  # Need explicit condition
        if nums[left] != nums[right]:
            left += 1
            nums[left] = nums[right]
        right += 1  # Must increment manually!
    
    return left + 1

"""
# Using while loops takes more lines of code so using for loop is appropriate

# Use for loop: When you need to iterate through all elements (linear scan)

# Use while loop: When pointers move in different ways/directions (converging, diverging, or conditional movement)
        
