# Finding floor and ceil
# Using Binary Search Among 3 comparisons
# Floor (sKey == & >) , Ceil(sKey == & <) is used
Using GPT# def findFloor(self, arr, N, X):
#         ans = -1
#         start = 0
#         end = N - 1
        
#         while start <= end:
#             mid = (start + end) // 2
#             if arr[mid] <= X:
#                 ans = mid
#                 start = mid + 1
#             else:
#                 end = mid - 1
                
#         return ans

def findFloor(arr, n, x):
    start = 0
    end = n - 1
    ans = -1
    while start < end:
        mid = (start + end)//2
        if arr[mid] <= x:
            ans  = arr[mid]
            start = mid + 1
        else:
            end = mid - 1
    return ans

def findCeil(arr, n, x):
    start = 0
    end = n - 1
    ans = -1
    while start <= end:
        mid = (start + end)//2
        if arr[mid] >= x:
            ans = arr[mid]
            end = mid - 1
        else:
            start = mid + 1
    return ans

def getFloorAndCeil(arr, n, x):
    f = findFloor(arr, n, x)
    c = findCeil(arr, n, x)
    return (f, c)
# Driver code
arr = [3, 4, 4, 7, 8, 10]
n = 6
x = 5
ans = getFloorAndCeil(arr, n, x)
print("The floor and ceil are:", ans[0], ans[1])