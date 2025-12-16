def main():
    x = int(input())  # Remove the prompt text
    if is_even(x):
        print("Even")
    else:
        print("Odd")

def is_even(n):
    return n % 2 == 0

main()