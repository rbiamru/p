#GPT Binary search
class Solution:
    def findKRotation(self, arr, n):
        start = 0
        end = n - 1
        
        while start <= end:
            mid = (start + end) // 2
            next = (mid + 1) % n
            
            # Check if the next element is smaller than the current element
            if arr[mid] > arr[next]:
                return (mid + 1) % n  # Return the index of the next element
            
            # Adjust the start and end pointers based on the rotation point
            elif arr[start] <= arr[mid]:
                start = mid + 1
            else:
                end = mid - 1
        
        # If no rotation point is found, return 0
        return 0
# Find number of rotations in a sorted rotated array
# # Using brute force method
# def countRotations(arr, n):
#     min_arr = arr[0]
#     min_arr_index = 0
#     for i in range(n):
#         if arr[i] < min_arr:
#             min_arr = arr[i]
#             min_arr_index = i
#     return min_arr_index

# # Driver code
# arr = [15, 18, 2, 3, 6, 12]
# n = len(arr)
# print(countRotations(arr, n))

# #*******Using Linear Search(Pivot)
# def countRotations(arr, n):
#     if arr[0] > arr[n - 1]:
#         for i in range(0, n):
#             if arr[i] > arr[i + 1]:
#                 return i + 1
#     return 0
# # Driver code
# arr = [15, 18, 2, 3, 6, 12]
# n = len(arr)
# print(countRotations(arr, n))

# #********Using Pivot with Binary Search
# def countRotations(arr, n):
#     start = 0
#     end = n - 1
#     while start <= end:
#         mid = (start + end)//2
#         prev = (mid - 1 + n) % n
#         next = (mid + 1) % n
#         if arr[mid] < arr[prev] and arr[mid] <= arr[next]:
#             return mid
#         elif arr[mid] < arr[start]:#search in left
#             end = mid - 1
#         elif arr[mid] > arr[end]: #search in right
#             start = mid + 1
#         else:
#             return 0

# # Driver code
# if __name__ == "__main__":
#     arr = [15, 18, 2, 3, 6, 12]
#     N = len(arr)
#     print(countRotations(arr, N))

# # Using pivot with Binary Search
# def countRotations(arr, n):
    # start = 0
    # end = n - 1
    # while start <= end:
    #     mid = (start + end)//2
    #     prev = (mid - 1 + n) % n
    #     next = (mid + 1) % n
    #     if arr[mid] <= arr[prev] and arr[mid] <= arr[next]:
    #         return mid
    #     elif arr[mid] < arr[start]:
    #         end = mid - 1
    #     elif arr[mid] > arr[end]:
    #         start = mid + 1
    # return 0

# # Driver code
# if __name__ == "__main__":
#     arr = [15, 18, 2, 3, 6, 12]
#     n = len(arr)
#     print(countRotations(arr, n))

# # Using pivot function and binary search
# def countRotations(arr, n):
#     pivot = findPivot(arr, n)
#     return pivot + 1
# def findPivot(arr, n):
#     start = 0
#     end = n - 1
#     while start <= end:
#         mid = (start + end)//2
#         if mid < end and arr[mid] > arr[mid + 1]:
#             return mid
#         if mid > start and arr[mid - 1] > arr[mid]:
#             return mid - 1
#         if arr[start] > arr[mid]:
#             end = mid - 1
#         else:
#             start = mid + 1
#     return -1
# # Driver code
# if __name__ == "__main__":
#     arr = [15, 18, 2, 3, 6, 12]
#     n = len(arr)
#     print(countRotations(arr, n))