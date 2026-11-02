# Fibonacci using Non-Recursive Method (iterative method)

n = int(input("Enter number of terms: "))

a, b = 0, 1
count = 0

print("\nFibonacci Series (Non-Recursive):")

for i in range(n):
    print(a, end=" ")
    count += 1

    a, b = b, a + b
    count += 1

print("\nStep Count:", count)
print("Time Complexity: O(n)")
print("Space Complexity: O(1)")


# Fibonacci using Recursive Method

count = 0

def fibonacci(n):
    global count
    count += 1

    if n <= 1:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)


print("\nEnter number of terms:", n)
print("\nFibonacci Series (Recursive):")

for i in range(n):
    print(fibonacci(i), end=" ")

print("\nStep Count:", count)
print("Time Complexity: O(2^n)")
print("Space Complexity: O(n)")


"""
psuedocode:
START
Read n
Set a = 0, b = 1
Repeat n times:
    Print a
    c = a + b
    a = b
    b = c
STOP"""