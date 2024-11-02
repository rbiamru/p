# # Print matrix in diagonal order
# MAX = 100
def printMatrixDiagonal(mat, n):
    i = 0
    j = 0
    k = 0
    isUp = True
    while k < n * n:
        if isUp:
            while i >= 0 and j < n:
                print(str(mat[i][j]), end = " ")
                k += 1
                j += 1
                i -= 1
            
            if i < 0 and j <= n-1:
                i = 0
            if j == n:
                i = i + 2
                j -= 1
        else:
            while j >= 0 and i < n:
                print(mat[i][j], end = " ")
                k += 1
                i += 1
                j -= 1
            if j < 0 and i <= n - 1:
                j = 0
            if i == n:
                j = j + 2
                i -= 1
        isUp = not isUp
# Driver program
if __name__ == "__main__":
    mat = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]]
    n = 3
    printMatrixDiagonal(mat, n)

# Print matrix in diagonal order

# # Driver Code
# mat = [[1, 2, 3, 4],
#         [5, 6, 7, 8],
#         [9, 10, 11, 12],
#         [13, 14, 15, 16]];
# n = 4
# mode = 0
# it = 0
# lower = 0
# for t in range(2 * n -1):
#     t1 = t
#     if t1 >= n:
#         mode += 1
#         t1 = n - 1
#         it -= 1
#         lower += 1
#     else:
#         lower = 0
#         it += 1
#     for i in range(t1, lower - 1, -1):
#         if (t1 + mode)%2 == 0:
#             print(mat[i][t1 + lower - i])
#         else:
#             print(mat[t1 + lower - i][i])