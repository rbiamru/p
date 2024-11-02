# Find row with maximum number of 1s
class Solution:
    def findMaxRow(self, mat, N):
        
        # simple naive approach
        maxcount=0    #intialize count,ind, = 0
        index=0
        for i in range(N):
            count = mat[i].count(1)    #each row if 1 is occur count it
            if count >maxcount:
                maxcount=count
                index=i       #update the index to i
        return [index,maxcount]


# # Find row with maximum number of 1s

# R, C = 4, 4
# def first(arr, start, end):
#     if end >= start:
#         mid = (start + end)//2
#         if (mid == 0 or arr[mid - 1] == 0) and arr[mid] == 1:
#             return mid
#         elif arr[mid] == 0:
#             return first(arr, mid + 1, end)
#         else:
#             return first(arr, start, mid - 1)
#     return -1
        
# def rowWithMax1s(mat):
#     max_row_index, Max = 0, -1
#     for i in range(R):
#         index = first(mat[i], 0, C-1)
#         if index != -1 and C - index > Max:
#             Max = C - index
#             max_row_index = i
#     return max_row_index
# # Driver code
# mat = [[0, 0, 0, 1],
#        [0, 1, 1, 1],
#        [1, 1, 1, 1],
#        [0, 0, 0, 0]]
# print("Index of row with maximum 1s is " + str(rowWithMax1s(mat)))

# # Using 
# R, C = 4, 4
# def first(arr, start, end):
#     if end >= start:
#         mid = (start + end)//2
#         if (mid == 0 or arr[mid - 1] == 0) and arr[mid] == 1:
#             return mid
#         elif arr[mid] == 0:
#             return first(arr, mid + 1, end)
#         else:
#             return first(arr, start, mid - 1)
#     return -1
    
# def rowWithMax1s(mat):
#     max_row_index = 0
#     max = first(mat[0], 0, C -1)
#     for i in range(1, R):
#         if max != -1 and mat[i][C - max - 1] == 1:
#             index = first(mat[i], 0, C - max)
#             if index != -1 and C - index > max:
#                 max = C - index
#                 max_row_index = i
#             else:
#                 max = first(mat[i], 0, C - 1)
#     return max_row_index

# # Driver code
# mat = [[0, 0, 0, 1],
#        [0, 1, 1, 1],
#        [1, 1, 1, 1],
#        [0, 0, 0, 0]]
# print("Index of row with maximum 1s is", rowWithMax1s(mat))
 

# # Using 
# def first(arr, start, end):
#     if end >= start:
#         mid = (start + end)//2
#         if (mid == 0 or arr[mid - 1] == 0) and arr[mid] == 1:
#             return mid
#         elif arr[mid] == 0:
#             return first(arr, mid + 1, end)
#         else:
#             return first(arr, start, mid - 1)
#     return -1
# def rowWithMax1s(mat):
#     R = len(mat)
#     C = len(mat[0])
#     max_row_index = 0
#     max = -1
#     for i in range(0, R):
#         index = first(mat[i], 0, C - 1)
#         if index != -1 and C - index > max:
#             max = C - index
#             max_row_index = i
#     return max_row_index
# # Driver code
# mat = [[0, 0, 0, 1],
#        [0, 1, 1, 1],
#        [1, 1, 1, 1],
#        [0, 0, 0, 0]]
# print("Index of row with maximum 1s is", rowWithMax1s(mat))
