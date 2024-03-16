# Find minimum element in sorted and rotated array
# # Using brute force method
# def findMin(arr, N):
#     min_ele = arr[0]
#     for i in range(N):
#         if arr[i] < min_ele:
#             min_ele = arr[i]
#     return min_ele
# # Driver program
# arr = [5, 6, 1, 2, 3, 4]
# N = len(arr)
# print(findMin(arr, N))
# Using binary search
def findMin(arr, start, end):
    if arr[start] <= arr[end]:
        return arr[start]
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] < arr[mid - 1]:
            return arr[mid]
        if arr[mid] > arr[end]:
            start = mid + 1
        else:
            end = mid - 1
    return -1
# Driver code
if __name__ == "__main__":
    arr = [5, 6, 1, 2, 3, 4]
    N = len(arr)
    print("The minimum element is " + str(findMin(arr, 0, N - 1)))