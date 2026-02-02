""""
To find higest number from the array

"""
# First approach using max function given by python
numbers = [2,5,1,8,2,9,1]
number = int(input("Number?: "))
higest = max(numbers)

if number == higest:
    print(f"Higest number is: {higest}")
else: 
    print("Not higest number")

# Second approach sliding window