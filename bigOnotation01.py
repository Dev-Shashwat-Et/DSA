"""
Big O notation is used to measure how running time or space requirements
for your program grow as input size grows
"""


def get_squared_numbers(numbers):
    squared_numbers = []
    for n in numbers:
        squared_numbers.append(n*n)
    return squared_numbers 

numbers = [2, 5, 8, 9]
result = get_squared_numbers(numbers)
print(result)  # Output: [4, 25, 64, 81]





"""
Step 1: squared_numbers = []          # Empty container ready
Step 2: n = 2 → append(4) → [4]
Step 3: n = 5 → append(25) → [4, 25]
Step 4: n = 8 → append(64) → [4, 25, 64]  
Step 5: n = 9 → append(81) → [4, 25, 64, 81]
Step 6: return [4, 25, 64, 81]       # Final result

"""








