# Using GPT 
def nthRowOfPascalTriangle(self, n):
    mod=10**9+7
    result=[]
    for i in range(0,n):
        temp=[1]*(i+1)
        for j in range(1,i):
            temp[j]=(result[j-1]+result[j])%mod
        result=temp
    return temp


# Pascal triangle
# # Using binomial coefficient
# def printPascal(n):
#     for line in range(0, n):
#         for i in range(0, line + 1):
#             print(binomialCoeff(line, i), " ", end = "")
#         print()
# def binomialCoeff(n, k):
#     res = 1
#     if (k > n - k):
#         k = n - k
#     for i in range(0, k):
#         res = res * (n - i)
#         res = res // (i + 1)
#     return res
# # Driver program
# n = 7
# printPascal(n)
# # Using dynamic programming i.e. array
# def printPascal(n:int):
#     # initialise a 2D matrix with '0'
#     arr = [[0 for x in range(n)] for y in range(n)]
#     for line in range(0, n):
#         for i in range(0, line + 1):
#             if (i == 0 or i == line):
#                 arr[line][i] = 1
#                 print(arr[line][i], end = " ")
#             else:
#                 arr[line][i] = arr[line - 1][i - 1] + arr[line - 1][i]
#                 print(arr[line][i], end = " ")
#         print("\n", end = "")
# # Driver code
# n = 5
# printPascal(n)
# Using binomial coefficient with optimisation
def printPascal(n):
    for line in range(1, n + 1):
        c = 1
        for i in range(1, line + 1):
            print(c, end = " ")
            c = int(c * (line - i) / i)
        print("")
# Driver code
n = 5
printPascal(n)