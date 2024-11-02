# Find element in bitonic array using binary search
def ascendingBinarySearch(arr, start, end, key):
    while start <= end:
        mid = (start + end)//2
        if arr[mid] == key:
            return mid
        if arr[mid] > key:
            end = mid - 1
        else:
            start = mid + 1
    return -1
def descendingBinarySearch(arr, start, end, key):
    while start <= end:
        mid = (start + end)//2
        if arr[mid] == key:
            return mid
        if arr[mid] < key:
            end = mid - 1
        else:
            start = mid + 1
    return -1
def findBitonicPoint(arr, n, start, end):
    bitonicPoint = 0
    mid = (start + end)//2
    if arr[mid] > arr[mid - 1] and arr[mid] > arr[mid + 1]:
        return mid
    elif arr[mid] > arr[mid - 1] and arr[mid] < arr[mid + 1]:
        bitonicPoint = findBitonicPoint(arr, n, mid, end)
    else:
        bitonicPoint = findBitonicPoint(arr, n, start, mid)
    return bitonicPoint

def searchBitonic(arr, n, key, index):
    if key > arr[index]:
        return -1
    elif key == arr[index]:
        return index
    else:
        temp = ascendingBinarySearch(arr, 0, index - 1, key)
        if temp != -1:
            return temp
        return descendingBinarySearch(arr, index + 1, n - 1, key)
def main():
    arr = [-8, 1, 2, 3, 4, 5, -2, -3]
    key = 1
    n = len(arr)
    start = 0
    end = n - 1
    # Function call
    index = findBitonicPoint(arr, n, start, end)
    x = searchBitonic(arr, n, key, index)
    if x == -1:
        print("Element not found")
    else:
        print("Element found at index", x)
# Driver code
main()