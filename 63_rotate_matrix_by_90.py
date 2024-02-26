#Rotate matrix by 90 degree
# By using temp variable diamond shape
# def rotate90Clockwise(A):
#     N = len(A[0])
#     for i in range(N // 2):
#         for j in range(i, N - i - 1):
#             temp = A[i][j]
#             A[i][j] = A[N - 1 - j][i]
#             A[N - 1 - j][i] = A[N - 1 - i][N - 1 - j]
#             A[N - 1 - i][N - 1 - j] = A[j][N - 1 - i]
#             A[j][N - 1 - i] = temp 
# def printMatrix(A):
#     n = len(A[0])
#     for i in range(n):
#         print(A[i])

# # Driver code
# A = [[1, 2, 3, 4],
#      [5, 6, 7, 8],
#      [9, 10, 11, 12],
#      [13, 14, 15, 16]]
# rotate90Clockwise(A)
# printMatrix(A)

# # Using only for loops
# N = 4
# def rotate90Clockwise(arr):
#     global N
#     for j in range(N):
#         for i in range(N - 1, -1, -1):
#             print(arr[i][j], end=" ")
#         print()

# # Driver code
# arr = [[1, 2, 3, 4],
#        [5, 6, 7, 8],
#        [9, 10, 11, 12],
#        [13, 14, 15, 16]]
# rotate90Clockwise(arr);

# Using rotation along secondary diagonal and middle row
# N = 4
# def display(arr):
#     for i in range(N):
#         for j in range(N):
#             print(arr[i][j], end=" ")
#         print()
# # Function to rotate the matrix 90degree clockwise
# def rotate90Clockwise(arr):
#     global N
#     # secondary diagonal rotation
#     for i in range(N):
#         for j in range(N-i):
#             arr[i][j], arr[N-1-i][N - 1 - j] = arr[N - 1 - i][N - 1 -j], arr[i][j]
#     # middle row
#     for i in range(N // 2):
#         for j in range(N):
#             arr[i][j], arr[N - 1 -i][j] = arr[N - 1 - i][j], arr[i][j]

# #Driver code
# arr = [[1, 2, 3, 4], 
#         [5, 6, 7, 8],
#         [9, 10, 11, 12],
#         [13, 14, 15, 16]]
# rotate90Clockwise(arr)
# display(arr)

# Using transpose and reverse each rows
#Function to rotate matrix anticlockwise by 90 degrees.
def rotateby90(self,arr, N): 
        # Transpose the matrix
        for i in range(N):
            for j in range(i + 1, N):
                arr[i][j], arr[j][i] = arr[j][i], arr[i][j]
    
        # Reverse the rows
        for i in range(N // 2):
            arr[i], arr[N - 1 - i] = arr[N - 1 - i], arr[i]

# Driver code
if __name__ == '__main__':
    arr=[[1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]]
    rotateby90(arr)
    display(arr)
