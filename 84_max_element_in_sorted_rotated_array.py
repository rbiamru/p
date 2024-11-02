# Max element in sorted and rotated array
def findMax(arr, start, end):
    if end == start:
        return arr[start]
    mid = (start + end) // 2
    if (mid == 0 and arr[mid] > arr[mid + 1]):
        return arr[mid]
    if mid < end and arr[mid + 1] < arr[mid] and mid > 0 and arr[mid] > arr[mid - 1]:
        return arr[mid]
    
    if arr[start] > arr[mid]:
        return findMax(arr, start, mid - 1)
    else:
        return findMax(arr, mid + 1, end)

# Driver code
arr = [6, 5, 4, 3, 2, 1]
n = len(arr)
print(findMax(arr, 0, n - 1))