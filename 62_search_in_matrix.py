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
max = 100
def binarySearch(mat, i, j_low, j_high, x):
    while j_low <= j_high:
        j_mid = (j_low + j_high) // 2
        if mat[i][j_mid] == x:
            print("Found at", i, j_mid)
            return
        elif mat[i][j_mid] > x:
            j_high = j_mid - 1
        else:
            j_low = j_mid + 1
    print("Element not found")
def sortedMatrixSearch(mat, n, m, x):
    if n == 1:
        binarySearch(mat, 0, 0, m-1, x)
        return
    i_low = 0
    i_high = n -1
    j_mid = m // 2
    while i_low + 1 < i_high:
        i_mid = (i_low + i_high) // 2
        if mat[i_mid][j_mid] == x:
            print("Found at", i_mid, j_mid)
            return
        elif mat[i_mid][j_mid] > x:
            i_high = i_mid
        else:
            i_low = i_mid
    if mat[i_low][j_mid] == x:
        print("Found at", i_low, j_mid)
    elif mat[i_low + 1][j_mid] == x:
        print("Found at", i_low+1, j_mid)
    elif x <= mat[i_low][j_mid-1]:
        binarySearch(mat, i_low, 0, j_mid - 1, x)
    elif x >= mat[i_low][j_mid + 1] and x <= mat[i_low][m-1]:
        binarySearch(mat, i_low, j_mid+1, m-1, x)
    elif x <= mat[i_low + 1][j_mid - 1]:
        binarySearch(mat, i_low + 1, 0, j_mid - 1, x)
    else:
        binarySearch(mat, i_low + 1, j_mid + 1, m - 1, x)
if __name__ == "__main__":
    n = 4
    m = 5
    x = 8
    mat = [[0, 6, 8, 9, 11], 
           [20, 22, 28, 29, 31],
           [36, 38, 50, 61, 63],
           [64, 66, 100, 122, 128]]
    sortedMatrixSearch(mat, n, m, x)
