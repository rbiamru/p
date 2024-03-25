# Allocate minimum number of pages
def isPossible(arr, n, m, curr_min):
    studentsRequired = 1
    curr_sum = 0
    for i in range(n):
        if arr[i] > curr_min:
            return False
        if curr_sum + arr[i] > curr_min:
            studentsRequired += 1
            curr_sum = arr[i]
            if studentsRequired > m:
                return False
        else:
            curr_sum += arr[i]
    return True

def findPages(arr, n, m):
    sum = 0
    if n < m:
        return -1
    for i in range(n):
        sum += arr[i]
    start, end = 0, sum
    result = 10 ** 9
    while start <= end:
        mid = (start + end)//2
        if isPossible(arr, n, m, mid):
            result = mid
            end = mid - 1
        else:
            start = mid + 1
    return result
# Driver code
arr = [12, 34, 67, 90]
n = len(arr)
m = 2 # Number of students
print("Minimum number of pages = ", findPages(arr, n, m))