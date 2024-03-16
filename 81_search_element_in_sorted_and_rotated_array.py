# Search element in sorted and rotated array
# Using binary search (recursion)
# def search(arr, start, end, sKey):
#     if start > end:
#         return -1
#     mid = (start + end) // 2
#     if arr[mid] == sKey:
#         return mid
#     if arr[start] == arr[mid] and arr[end] == arr[mid]:
#         start += 1
#         end -= 1
#         return search(arr, start, end, sKey)
#     if arr[start] <= arr[mid]:
#         if sKey >= arr[start] and sKey <= arr[mid]:
#             search(arr, start, mid - 1, sKey)
#         return search(arr, mid + 1, end, sKey)
#     if sKey >= arr[mid] and sKey <= arr[end]:
#         return search(arr, mid + 1, end, sKey)
#     return search(arr, start, mid - 1, sKey)
# # Driver code
# if __name__ == "__main__":
#     arr = [3, 3, 1, 2, 3, 3]
#     n = len(arr)
#     sKey = 3
#     print(search(arr, 0, n - 1, sKey))

# Using binary search (to save auxiliary space)
def search(arr, start, end, sKey):
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == sKey:
            return mid
        if arr[mid] == arr[start] and arr[mid] == arr[end]:
            start += 1
            end -= 1
            continue
        if arr[start] <= arr[mid]:
            if sKey < arr[mid] and sKey >= arr[start]:
                end = mid - 1
            else:
                start = mid + 1
        else:
            if sKey > arr[mid] and sKey <= arr[end]:
                start = mid + 1
            else:
                end = mid - 1
    return -1
# Driver code
arr = [3, 3, 1, 2, 3, 3]
n = len(arr)
sKey = 3
print(search(arr, 0, n - 1, sKey))