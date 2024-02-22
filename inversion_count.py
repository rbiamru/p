# Inversion count using merge sort
#******* Using Brute Force Method
# def getInvCount(arr, n):
#     inv_count = 0
#     for i in range(n):
#         for j in range(i+1, n):
#             if arr[i] > arr[j]:
#                 inv_count += 1
#     return inv_count

# # Driver code
# arr = [1, 20, 6, 4, 5]
# n = len(arr)
# print("Number of inversions are", getInvCount(arr, n))

#********* Using merge sort
def mergeSort(arr, n):
    temp_arr = [0] * n
    return _mergeSort(arr, temp_arr, 0, n-1)
def _mergeSort(arr, temp_arr, left, right):
    inv_count = 0
    if left < right:
        mid = (left + right)//2
        inv_count += _mergeSort(arr, temp_arr, left, mid)
        inv_count += _mergeSort(arr, temp_arr, mid+1, right)
        inv_count += merge(arr, temp_arr, left, mid, right)
    return inv_count
def merge(arr, temp_arr, left, mid, right):
    i = left
    j = mid + 1
    k = left
    inv_count = 0
    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp_arr[k] = arr[i]
            k += 1
            i += 1
        else:
            temp_arr[k] = arr[j]
            inv_count += (mid - i + 1)
            k += 1
            j += 1
    while i <= mid:
        temp_arr[k] = arr[i]
        k += 1
        i += 1
    while j <= right:
        temp_arr[k] = arr[j]
        k += 1
        j += 1
    for loop_var in range(left, right + 1):
        arr[loop_var] = temp_arr[loop_var]
    return inv_count        
# # Driver code
# arr = [1, 20, 6, 4, 5]
# n = len(arr)
# result = mergeSort(arr, n)
# print("Number of inversions are", result)
# # Using heap and bisect
# from heapq import heappush, heappop
# from bisect import bisect, insort
# def getNumofInversions(A):
#     N = len(A)
#     if N <= 1:
#         return 0
#     sortList = []
#     result = 0
#     # Using Heapsort for arranging in ascending order
#     for i,v in enumerate(A):
#         heappush(sortList, (v, i))
#     # Create a sorted list of indexes
#     x = []
#     while sortList:
#         v, i = heappop(sortList)
#         # bisect i can be inserted at y position in x array
#         # insort i is inserted in x array
#         y = bisect(x, i)
#         result += i - y
#         insort(x, i)
#     return result


# # Driver Code
# if __name__ == '__main__':
#     A = [1, 20, 6, 4, 5]
#     result = getNumofInversions(A)
#     print(f'Number of inversions are {result}')