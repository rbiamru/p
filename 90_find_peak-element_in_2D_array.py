# # Search peak elements in 2D array
# # Using naive approach
# def findPeakGrid(arr):
#     result = []
#     row = len(arr)
#     column = len(arr[0])
#     for i in range(row):
#         for j in range(column):
#             if i > 0:
#                 if arr[i][j] < arr[i - 1][j]:
#                     continue
#             if j < column - 1:
#                 if arr[i][j] < arr[i][j + 1]:
#                     continue
#             if i < row - 1:
#                 if arr[i][j] < arr[i + 1][j]:
#                     continue
#             if j > 0:
#                 if arr[i][j] < arr[i][j - 1]:
#                     continue
#             result.append(i)
#             result.append(j)
#             break
#     return result
# # Driver code
# arr = [[9, 8],
#         [2, 6]]
# result = findPeakGrid(arr)
# print("Peak element found at index:", result)
# Using binary search
def findPeakGrid(mat):
    start = 0
    end = len(mat[0]) - 1
    while start <= end:
        mid = start + int((end - start)/2)
        ansrow = 0
        for r in range(len(mat)):
            ansrow = r if mat[r][mid] >= mat[ansrow][mid] else ansrow
        valid_left = mid - 1 >= start and mat[ansrow][mid - 1] > mat[ansrow][mid]
        valid_right = mid + 1 <= end and mat[ansrow][mid + 1] > mat[ansrow][mid]
        if (not valid_left and not valid_right):
            return [ansrow, mid]
        elif valid_right:
            start = mid + 1
        else:
            end = mid - 1
    return [-1, -1]
# Driver code
arr = [[9, 8],
       [2, 6]]
result = findPeakGrid(arr)
print("Peak element found at index:", result)