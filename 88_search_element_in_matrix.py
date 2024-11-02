# # Search element in matrix
# def search(mat, n, x):
#     if n == 0:
#         return -1
#     for i in range(n):
#         for j in range(n):
#             if mat[i][j] == x:
#                 print("Element found at (", i, ",", j, ")")
#                 return 1
#     print("Element not found")
#     return 0        
# # Driver code
# if __name__ == "__main__":
#     mat = [[10, 20, 30, 40],
#            [15, 25, 35, 45],
#            [27, 29, 37, 48],
#            [32, 33, 39, 50]]
#     search(mat, 4, 29)
# # Search element at the rightmost corner of the array
def search(mat, n, sKey):
    i = 0
    j = n - 1
    while i < n and j >= 0:
        if mat[i][j] == sKey:
            print("Element is found at", i, ", ", j)
            return 1
        if mat[i][j] > sKey:
            j -= 1
        else:
            i += 1
    print("Element not found")
    return 0
# # Driver code
# if __name__ == "__main__":
#     mat = [[10, 20, 30, 40],
#            [15, 25, 35, 45],
#            [27, 29, 37, 48],
#            [32, 33, 39, 50]]
#     search(mat, 4, 29)
# # Using Linear search
# def search_element(mat, x):
#     for i in range(len(mat)):
#         for j in range(len(mat[0])):
#             if mat[i][j] == x:
#                 return f"Found at ({i}, {j})"
#     return "Element not found"
# # Driver code
# mat = [[10, 20, 30, 40], 
#        [15, 25, 35, 45], 
#        [27, 29, 37, 48], 
#        [32, 33, 39, 50]]
# x = 29
# print(search_element(mat, x))
# x = 100
# print(search_element(mat, x))
