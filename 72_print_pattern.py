# Using GPT
def pattern(self, N):
        curval = N
        result = []
        result.append(N)
        while N>0:
            N-= 5
            result.append(N)
        while N != curval:
            N+=5
            result.append(N)
        return result
        
# # Print diamond pattern
# # Using brute force
# # i > n - j + 1   | i < j
# # j < n + i - 1   | i < 2 * n - j
# def pattern(n):
#     # Upper half of pattern
#     for i in range(1, n + 1):
#         for j in range(1, 2 * n):
#             if i > n - j + 1:
#                 print("", end = " ")
#             else:
#                 print("*", end="")
#             if i + n - 1 > j:
#                 print("", end = " ")
#             else:
#                 print("*", end = "");
#         print("");
#     # Lower half of pattern
#     for i in range(1, n + 1):
#         for j in range(1, 2 * n):
#             if i < j:
#                 print("", end = " ")
#             else:
#                 print("*", end = "")
#             if i < 2 * n - j:
#                 print("", end = " ")
#             else:
#                 print("*", end = "")
#         print("")


# # Driver code
# pattern(7)

# Draw broken diamond
# # Using brute force method
# def pattern(n):
#     for i in range(1, n + 1):
#         for j in range(1, 2 * n + 1):
#             if i < j:
#                 print("", end = " ")
#             else:
#                 print("*", end="")
#             if i <= 2 * n - j:
#                 print("", end = " ")
#             else:
#                 print("*", end="")
#         print("")
#     for i in range(1, n + 1):
#         for j in range(1, 2 * n + 1):
#             if i > n - j + 1:
#                 print("", end = " ")
#             else:
#                 print("*", end = "")
#             if j < i + n:
#                 print("", end = " ")
#             else:
#                 print("*", end = "")
#         print("")

# # Driver code
# pattern(7)

# # Draw X in star
# def pattern(n):
#     for i in range(1, n+1):
#         for j in range(1, n + 1):
#             if i == j or i + j == n + 1:
#                 if i + j == n + 1:
#                     print("/", end = "")
#                 else:
#                     print("\\", end = "")
#             else:
#                 print("*", end = "")
#         print("")

# # Driver code
# if __name__ == "__main__":
#     n = 8
#     pattern(n)

# # Number Pattern
# def pattern(n):
#     for i in range(n - 1, -1, -1):
#         for j in range(i, -1, -1):
#             print(j, end = " ")
#         print("")
# # Driver code
# if __name__ == "__main__":
#     n = 8
#     pattern(n)

# Number Pattern 2
def pattern(n):
    k = 1
    for i in range(1, n + 1):
        p = k
        for j in range(1, i + 1):
            print(p, end = " ")
            p = p - (n - i + j)
        print()
        k = k + 1 + (n - i)
# Driver code
if __name__ == "__main__":
    n = 7
    pattern(n)