

def removeDuplicates(nums):
    result = []
    for num in nums:
        if num not in result:
            result.append(num)
    
    for i in range(len(result)):
        nums[i] = result[i]  # This modifies nums!
    
    return len(result)  # This returns ONLY 3 (the number)

# Testing:
nums = [1, 1, 2, 2, 3]
k = removeDuplicates(nums)
print(nums[:k])  # ← THIS LINE shows [1, 2, 3]!,nums[:k] = nums[0:3] = [nums[0], nums[1], nums[2]] = [1, 2, 3]

# Time coplexity of this program is O(n^2) and space complexity is O