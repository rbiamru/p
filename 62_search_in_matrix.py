# Search in matrix
# # Using brute force method and dictionary
# n = 4 # no. of rows
# m = 5 # no. of columns
# a = [[0, 6, 8, 9, 11], 
#     [20, 22, 28, 29, 31],
#     [36, 38, 50, 61, 63],
#     [64, 66, 100, 122, 128]]
# k = 31 
# mp = {}
# for i in range(n):
#     for j in range(m):
#         if k == a[i][j]:
#             print("Found at (", i, ",", j, ")")
#     mp[a[i][j]] = [i, j]

# if k in mp:
#     print("This is how we can find using mapping: ")
#     print("(", mp[k][0], ",", mp[k][1], ")")
# else:
#     print("Not found")
# Using binary search in matrix
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binarySearch(arr, low, high, target):
            while low <= high:
                mid = (low + high) // 2
                if arr[mid] == target:
                    return True
                elif arr[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
            return False
        
        rows = len(matrix)
        if rows == 0:
            return False
        cols = len(matrix[0])
        if cols == 0:
            return False
        
        row = 0
        col = cols - 1
        
        while row < rows and col >= 0:
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                row += 1
            else:
                col -= 1
        
        return False
if __name__ == "__main__":
    n = 4
    m = 5
    x = 8
    mat = [[0, 6, 8, 9, 11], 
           [20, 22, 28, 29, 31],
           [36, 38, 50, 61, 63],
           [64, 66, 100, 122, 128]]
    searchMatrix(mat, n, m, x)
