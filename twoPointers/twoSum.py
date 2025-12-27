# Find the pair of two numbers from the array that matches the target sum of 15 from the given array = array = [1, 2, 3, 5, 7, 10, 11, 15]

def sum_of_pairs(arr, target):
    left, right = 0, len(arr)-1
    result = []
    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target:
            result.append((arr[left], arr[right]))
            left += 1 # Move left pointer RIGHT to check for other pairs
            right -= 1 # # Move left pointer LEFT to check for other pairs
        elif current_sum < target:
            left += 1 # Moves the left pinter
        else:
            right -= 1 # Moves the right pointer
    return result
    
print(sum_of_pairs([1, 2, 3, 5, 7, 10, 11, 15], 15))
print(sum_of_pairs([1, 2, 3, 4, 5, 6, 7, 8, 9], 10))

        
