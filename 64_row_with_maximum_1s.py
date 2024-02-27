

# # Row with maximum 1s in a matrix
# Easy solution

class Solution:
    #Function to find the row with minimum number of 1s.
    def minRow(self,N,M,A):
        mn,mni=1000000,-1
        
        #iterating over all the rows.
        for i in range(N):
            c=0
            
            #counting number of 1s in the current row.
            for j in range(M):
                if A[i][j]==1:
                    c+=1
            
            #checking if the current row has minimum number of 1s.
            if mn>c:
                mn=c
                mni=i+1
        
        #returning the row index with minimum number of 1s.
        return mni

# # Using recursion
# R = 4
# C = 4
# #2
# def first(arr, low, high):
#     if high >= low:
#         mid = low + (high - low)//2
#         if (mid == 0 or arr[mid-1] == 0) and arr[mid] == 1:
#             return mid
#         elif arr[mid] == 0:
#             return first(arr, mid + 1, high)
#         else:
#             return first(arr, low, mid - 1)
#     return -1
# # 1
# def rowWithMax1s(mat):
#     max_row_index, Max = 0, -1
#     for i in range(R):
#         index = first(mat[i], 0, C-1)
#         if index != -1 and C-index > Max:
#             Max = C - index
#             max_row_index = i
#     return max_row_index
    

# # Driver code
# mat = [[0, 0, 0, 1],
#        [0, 1, 1, 1],
#        [1, 1, 1, 1],
#         [0, 0, 0, 0]]
# print("Index of row with maximum 1s is " + str(rowWithMax1s(mat)))

# # Using binary search
# def first(arr, low, high):
#     if high >= low:
#         mid = low + (high - low)//2
#         if (mid == 0 or arr[mid-1] ==0) and arr[mid]==1:
#             return mid
#         elif arr[mid] == 0:
#             return first(arr, mid + 1, high)
#         else:
#             return first(arr, low, mid - 1)
#     return -1
# def rowWithMax1s(mat):
#     R = len(mat)
#     C = len(mat[0])
#     max_row_index = 0
#     max = -1
#     for i in range(0, R):
#         index = first(mat[i], 0, C-1)
#         if index != -1 and C - index > max:
#             max = C - index
#             max_row_index = i
#     return max_row_index

# # Driver code
# mat = [[0, 0, 0, 1], 
#        [0, 1, 1, 1],
#        [1, 1, 1, 1],
#        [1, 1, 1, 1]]
# print("Index of row with maximum 1s is", rowWithMax1s(mat))

# # # Using binary search with optimisation
# def first(arr, low, high):
#     if high >= low:
#         mid = low + (high - low)//2
#         if (mid == 0 or arr[mid-1] ==0) and arr[mid]==1:
#             return mid
#         elif arr[mid] == 0:
#             return first(arr, mid + 1, high)
#         else:
#             return first(arr, low, mid - 1)
#     return -1
# def rowWithMax1s(mat):
#     R = len(mat)
#     C = len(mat[0])
#     # Initialize max using values from first row.
#     max_row_index = 0
#     max = first(mat[0], 0, C - 1)

#     # Traverse for each row and count number of 1s
#     # by finding the index of first 1
#     for i in range(1, R):

#         # Count 1s in this row only if this row
#         # has more 1s than max so far

#         # Count 1s in this row only if this row
#         # has more 1s than max so far
#         if (max != -1 and mat[i][C - max - 1] == 1):

#             # Note the optimization here also
#             index = first(mat[i], 0, C - max)

#             if (index != -1 and C - index > max):
#                 max = C - index
#                 max_row_index = i
#         else:
#             max = first(mat[i], 0, C - 1)

#     return max_row_index


# # Driver code
# mat = [[0, 0, 0, 1], 
#        [0, 1, 1, 1],
#        [1, 1, 1, 1],
#        [1, 1, 1, 1]]
# print("Index of row with maximum 1s is", rowWithMax1s(mat))

# # Using optimisation
# def rowWithMax1s(mat):
#     R = len(mat)
#     C = len(mat[0])
#     max_row_index = 0
#     index = C - 1
#     for i in range(0, R):
#         flag = False
#         while(index >= 0 and mat[i][index] == 1):
#             flag = True
#             index -= 1
#             if flag:
#                 max_row_index = i
#         if max_row_index == 0 and mat[0][C-1] == 0:
#             return 0
#     return max_row_index

# #Driver code
# mat = [[0, 0, 0, 1],
#        [0, 1, 1, 1],
#        [1, 1, 1, 1],
#        [0, 0, 0, 0]]
# print("Index of row with maximum 1s is", rowWithMax1s(mat))
# class Solution:
#     def first(self, arr, low, high):
#         if high >= low:
#             mid = low + (high - low) // 2
#             if (mid == 0 or arr[mid - 1] == 0) and arr[mid] == 1:
#                 return mid
#             elif arr[mid] == 0:
#                 return self.first(arr, mid + 1, high)
#             else:
#                 return self.first(arr, low, mid - 1)
#         return -1

#     def minRow(self, R, C, mat):
#         max_row_index, Max = -1, -1  # Initialize max_row_index and Max
#         for i in range(R):
#             index = self.first(mat[i], 0, C - 1)
#             print("Row:", i, "Index of first 1:", index)
#             if index != -1 and C - index > Max:
#                 Max = C - index
#                 max_row_index = i
#             print("Current max_row_index:", max_row_index)
#             print("Current Max:", Max)
#         return max_row_index if max_row_index != -1 else 0

# # Test the solution
# sol = Solution()
# R, C = 4, 4
# mat = [
#     [1, 1, 1, 0],
#     [1, 1, 0, 0],
#     [0, 0, 1, 1],
#     [1, 1, 1, 1]
# ]
# print(sol.minRow(R, C, mat))
