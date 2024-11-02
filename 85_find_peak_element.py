# # Find peak element
# def findPeak(arr, n):
#     if n == 1:
#         return 0
#     if arr[0] >= arr[1]:
#         return 0
#     elif arr[n - 1] >= arr[n - 2]:
#         return n - 1
#     for i in range(1, n - 1):
#         if arr[i] >= arr[i + 1] and arr[i] >= arr[i - 1]:
#             return i
# # Driver code
# arr = [1, 3, 20, 4, 1, 0]
# n = len(arr)
# print("Index of a peak point is", findPeak(arr, n))

# #*******Find peak element using binary search(recursion)
# def findPeakUtil(arr, start, end, n):
#     mid = (start + end)//2
#     if (mid == 0 or arr[mid - 1] <= arr[mid]) and (mid == n - 1 or arr[mid + 1] <= arr[mid]):
#         return mid
#     elif (mid > 0 and arr[mid - 1] > arr[mid]):
#         return findPeakUtil(arr, start, mid - 1, n)
#     else:
#         return findPeakUtil(arr, mid + 1, end, n)
# def findPeak(arr, n):
#     return findPeakUtil(arr, 0, n - 1, n)
# # Driver code
# arr = [1, 3, 20, 4, 1, 0]
# n = len(arr)
# print("Index of a peak point is", findPeak(arr, n))

# Find peak element using binary seach(iteration)
def findPeak(arr, n):
    start = 0
    end = n - 1
    while start <= end:
        mid = (start + end) >> 1
        if (mid == 0 or arr[mid - 1] <= arr[mid]) and (mid == n - 1 or arr[mid + 1] <= arr[mid]):
            break
        if mid > 0 and arr[mid - 1] > arr[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return mid
# Driver code
arr = [1, 3, 20, 4, 1, 0]
n = len(arr)
print(f"Index of a peak point is {findPeak(arr, n)}")