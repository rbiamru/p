# Find factorial of a number
# Using recursion
# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n - 1)

# # Driver Code
# num = 5
# print("Factorial of", num, "is", factorial(num))
# Using iteration
# def factorial(n):
#     fact = 1
#     for i in range(1, n+1):
#         fact = fact * (i)
#     return fact

# # Driver Code
# num = 5
# print("Factorial of", num, "is", factorial(num))

# # Using while iteration
# def factorial(n):
#     if n == 0:
#         return 1
#     i = n
#     fact = 1
#     while (n/i != n):
#         fact = fact * i
#         i -= 1
#     return fact
#     # fact = 1
#     # while (n > 1):
#     #     fact *= n * (n - 1)
#     #     n = n - 2
#     # return fact

# # Driver Code
# num = 5;
# print("Factorial of", num, "is", factorial(num))

# Using ternary operator
def factorial(n):
    return 1 if (n == 0 or n ==1) else n * factorial(n - 1)
# Driver code
if __name__ == "__main__":
    num = 5
    print("Factorial of", num, "is", factorial(num))