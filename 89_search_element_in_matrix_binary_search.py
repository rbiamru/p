# Working from GPT
class Solution:
    def searchMatrix(self, mat: List[List[int]], target: int) -> bool:
        
        m=len(mat)
        n=len(mat[0])
        
        for i in range(m):
            if mat[i][0]<=target and mat[i][-1]>=target:
                lo=0
                hi=n
                while (lo<hi):
                    mid=(lo+hi)//2
                    
                    if mat[i][mid]==target:
                        return True
                    elif mat[i][mid]<target:
                        lo = mid + 1
                    else:
                        hi = mid
                        
        return False

# # Search an element in the given 2D - matrix using Binary Search
# M = 3
# N = 4
# def binarySearch1D(arr, K):
#     start = 0
#     end = N - 1
#     while start <= end:
#         mid = start + int((end - start) / 2)
#         if arr[mid] == K:
#             return True
#         if arr[mid] < K:
#             start = mid + 1
#         else:
#             end = mid - 1
#     return False
# def searchMatrix(matrix, K):
#     start = 0
#     end = M - 1
#     while start <= end:
#         mid = start + int((end - start)/2)
#         if K >= matrix[mid][0] and K <= matrix[mid][N - 1]:
#             return binarySearch1D(matrix[mid], K)
#         if K < matrix[mid][0]:
#             end = mid - 1
#         else:
#             start = mid + 1
#     return False

# # Driver code
# if __name__ == "__main__":
#     matrix = [[1, 3, 5, 7],
#               [10, 11, 16, 20],
#               [23, 30, 34, 50]]
#     K = 3
#     if searchMatrix(matrix, K):
#         print("Found")
#     else:
#         print("Not found")