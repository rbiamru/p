# First and last occurrences of x
# # Using brute force method
# def findFirstAndLast(arr, n, x):
#     first = -1
#     last = -1
#     for i in range(0, n):
#         if(x != arr[i]):
#             continue
#         if(first == -1):
#             first = i
#         last = i
#     if(first != -1):
#         print("First occurrence = ", first, " \n Last occurrence = ", last)
#     else:
#         print("Not found")
# # Driver code
# arr = [1, 2, 2, 2, 2, 3, 4, 7, 8, 8]
# n = len(arr)
# x = 8
# findFirstAndLast(arr, n, x)
# # Using binary search method
# def first(arr, start, end, sKey, n):
#     if end >= start:
#         mid = (start) + (end - start)//2
#         if((mid == 0 or sKey > arr[mid - 1]) and sKey == arr[mid]):
#             return mid
#         elif(sKey > arr[mid]):
#             return first(arr, mid + 1, end, sKey, n)
#         else:
#             return first(arr, start, mid - 1, sKey, n)
#     return -1

# def last(arr, start, end, sKey, n):
#     if end >= start:
#         mid = start + (end - start)//2
#         if ((mid == n -1 or sKey < arr[mid - 1]) and arr[mid] == sKey):
#             return mid
#         elif (sKey < arr[mid]):
#             return last(arr, start, mid - 1, sKey, n)
#         else:
#             return last(arr, mid + 1, end, sKey, n)
#     return -1

# # Driver program
# arr = [1, 2, 2, 2, 2, 3, 4, 7, 8, 8]
# n = len(arr)
# sKey = 8
# print("First occurrence = ", first(arr, 0, n - 1, sKey, n))
# print("Last occurrence = ", last(arr, 0, n - 1, sKey, n))

# # Using Binary search method - 2
# def first(arr, sKey, n):
#     start = 0
#     end = n - 1
#     res = -1
#     while start <= end:
#         mid = (start + end)//2
#         if sKey > arr[mid]:
#             start = mid + 1
#         elif sKey < arr[mid]:
#             end = mid - 1
#         else:
#             res = mid 
#             end = mid - 1
#     return res
# def last(arr, sKey, n):
#     start = 0
#     end = n - 1
#     res = -1
#     while start <= end:
#         mid = (start + end)//2
#         if sKey > arr[mid]:
#             start = mid + 1
#         elif sKey < arr[mid]:
#             end = mid - 1
#         else:
#             res = mid 
#             start = mid + 1
#     return res
# # Driver code
# arr = [1, 2, 2, 2, 2, 3, 4, 7, 8, 8]
# n = len(arr)
# x = 8
# print("First Occurrence =", first(arr, x, n))
# print("Last occurrence =", last(arr, x, n))

# # Using inbuilt functions
# def first(arr, start, end, sKey, n):
#     return arr.index(sKey)
# def last(arr, start, end, sKey, n):
#     return n - 1 - arr[::-1].index(sKey)
# #Driver code
# arr = [1, 2, 2, 2, 2, 3, 4, 7, 8, 8]
# n = len(arr)
# sKey = 8
# print("First occurrence of ", sKey, " = ", first(arr, 0, n-1, sKey, n))
# print("Last occurrence of", sKey, " = ", last(arr, 0, n - 1, sKey, n))

# Using binary search 3
def search(arr, sKey, findStartIndex):
    ans = -1
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = start + (end - start)//2
        if sKey < arr[mid]:
            end = mid - 1
        elif sKey > arr[mid]:
            start = mid + 1
        else:
            ans = mid
            if findStartIndex:
                end = mid - 1
            else:
                start = mid + 1
    return ans
# Driver code
arr = [1, 2, 2, 2, 2, 3, 4, 7, 8, 8]
n = len(arr)
sKey = 8
ans = [-1, -1]
ans[0] = search(arr, sKey, True)
if ans[0] != -1:
    ans[1] = search(arr, sKey, False)
print("First occurrence =", ans[0])
print("Last occurrence =", ans[1])
