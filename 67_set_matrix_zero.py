# # Set matrix as zero
# # Brute Force Method
# def markRow(matrix, n, m, i):
#     for j in range(m):
#         if matrix[i][j] != 0:
#             matrix[i][j] = -1

# def markCol(matrix, n, m, j):
#     for i in range(n):
#         if matrix[i][j] != 0:
#             matrix[i][j] = -1
        
# def zeroMatrix(matrix, n, m):
#     for i in range(n):
#         for j in range(m):
#             if matrix[i][j] == 0:
#                 markRow(matrix, n, m, i)
#                 markCol(matrix, n, m, j)
#     for i in range(n):
#         for j in range(m):
#             if matrix[i][j] == -1:
#                 matrix[i][j] = 0
#     return matrix

# # Driver code
# if __name__ == "__main__":
#     matrix = [[1, 1, 1],
#               [1, 0, 1],
#               [1, 1, 1]]
#     n = len(matrix)
#     m = len(matrix[0])
#     ans = zeroMatrix(matrix, n, m)
#     print("The Final matrix is:")
#     for row in ans:
#         for ele in row:
#             print(ele, end=" ")
#         print()

# Better Approach
def zeroMatrix(matrix, n, m):
    row = [0] * n
    col = [0] * m
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                row[i] = 1
                col[j] = 1
    for i in range(n):
        for j in range(m):
            if row[i] or col[j]:
                matrix[i][j] = 0
    return matrix


# Driver code
if __name__ == "__main__":
    matrix = [[1, 1, 1],
              [1, 0, 1],
              [1, 1, 1]]
    n = len(matrix)
    m = len(matrix[0])
    ans = zeroMatrix(matrix, n, m)
    print("The Final matrix is:")
    for row in ans:
        for ele in row:
            print(ele, end=" ")
        print()

# Optimal approach
def zeroMatrix(matrix, n, m):
    col0 = 1
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                if j != 0:
                    matrix[0][j] = 0
                else:
                    col0 = 0
    for i in range(1, n):
        for j in range(1, m):
            if matrix[i][j] != 0:
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
    if matrix[0][0] == 0:
        for j in range(m):
            matrix[0][j] = 0
    if col0 == 0:
        for i in range(n):
            matrix[i][0] = 0
    return matrix

# Driver code
if __name__ == "__main__":
    matrix = [[1, 1, 1],
              [1, 0, 1],
              [1, 1, 1]]
    n = len(matrix)
    m = len(matrix[0])
    ans = zeroMatrix(matrix, n, m)
    print("The Final matrix is:")
    for row in ans:
        for ele in row:
            print(ele, end = " ")
        print()


