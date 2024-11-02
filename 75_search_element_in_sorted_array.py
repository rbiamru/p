# Using GPT binary search
def searchInSorted(self, arr, N, key):
        low = 0
        high = N - 1
        
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] == key:
                return 1
            elif arr[mid] < key:
                low = mid + 1
            else:
                high = mid - 1
                
        return -1

# #Search pivot and an element in sorted array
# # Using pivot search and binary search algo
# def pivotedBinarySearch(arr, n, key):
#     pivot = findPivot(arr, 0, n - 1)
#     if pivot == -1:
#         return binarySearch(arr, 0, n - 1, key)
#     if arr[pivot] == key:
#         return pivot
#     if arr[0] <= key:
#         return binarySearch(arr, 0, pivot - 1, key)
#     return binarySearch(arr, pivot + 1, n - 1, key)


# def findPivot(arr, low, high):
#     if high < low:
#         return -1
#     if high == low:
#         return low
#     mid = int((low + high)/2)
#     if mid < high and arr[mid] > arr[mid + 1]:
#         return mid
#     if mid > low and arr[mid] < arr[mid - 1]:
#         return (mid - 1)
#     if arr[low] >= arr[mid]:
#         return findPivot(arr, low, mid - 1)
#     return findPivot(arr, mid + 1, high)

# def binarySearch(arr, start, end, key):
#     if end < start:
#         return -1
#     mid = int((start + end)/2)
#     # Do 3 comparisons
#     if key == arr[mid]:
#         return mid
#     if key > arr[mid]:
#         return binarySearch(arr, mid + 1, end, key)
#     if key < arr[mid]:
#         return binarySearch(arr, start, mid - 1, key)

# # Driver code
# if __name__ == "__main__":
#     arr1 = [5, 6, 7, 8, 9, 10, 1, 2, 3]
#     n = len(arr1)
#     key = 3
#     print("Index of the element is: ", pivotedBinarySearch(arr1, n, key))

# # Using binary search for half sorted
# def binarySearch(arr, start, end, key):
#     if start > end:
#         return -1
#     mid = int((start + end)/2)
#     # 3 comparisons
#     if key == arr[mid]:
#         return mid
#     if arr[start] <= arr[mid]:
#         if key >= arr[start] and key <= arr[mid]:
#             return binarySearch(arr, start, mid - 1, key)
#         return binarySearch(arr, mid + 1, end, key)
#     if key >= arr[mid] and key <= arr[end]:
#         return binarySearch(arr, mid + 1, end, key)
#     return binarySearch(arr, start, mid - 1, key)

# # Driver code
# if __name__ == "__main__":
#     arr = [4, 5, 6, 7, 8, 9, 1, 2, 3]
#     key = 3
#     i = binarySearch(arr, 0, len(arr) - 1, key)
#     if i != -1:
#         print("Index: %d " %i)
#     else:
#         print("Key not found")

# # Using serial search or linear search
# def search_rotated_array(arr, key):
#     for i in range(len(arr)):
#         if arr[i] == key:
#             return i
#     return -1
# # Driver code
# arr = [5, 6, 7, 8, 9, 10, 1, 2, 3]
# key = 3
# index = search_rotated_array(arr, key)
# if index != -1:
#     print(f"Found at index {index}")
# else:
#     print("Not found")