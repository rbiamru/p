# Search for element in an infinite array
# Using binary search
def binarySearch(arr, start, end, sKey):
    while start <= end:
        mid = (start + end) // 2
        if sKey == arr[mid]:
            return mid
        elif sKey > arr[mid]:
            start = mid + 1
        else:
            end = mid - 1
def findIndex(arr, sKey):
    start = 0
    end = 1
    while(arr[end] < sKey):
        start = end
        end = 2 * end
    return binarySearch(arr, start, end, sKey)
# Driver code
if __name__ == "__main__":
    arr = [3, 5, 7, 9, 10, 90, 100, 130, 140, 160, 170]
    ans = findIndex(arr, 130)
    print("Element is found at index", ans)

# Coding ninjas new format
def firstOne(get):
    # Initialize the leftmost and rightmost indices
    left, right = 0, 1

    # Find the range where the first occurrence of 1 might lie
    while get(right) == 0:
        left = right
        right *= 2

    # Perform binary search within the identified range
    while left <= right:
        mid = (left + right) // 2
        if get(mid) == 1:
            if mid == 0 or get(mid - 1) == 0:
                return mid  # Found the first occurrence of 1
            else:
                right = mid - 1  # Move left to find the first occurrence
        else:
            left = mid + 1  # Move right
