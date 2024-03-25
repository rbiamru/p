# Distance the aggressive cows
# def ok(arr, x, K):
#     n = len(arr)
#     count = 1
#     arr.sort()  # Sort the array initially
#     start = arr[0]
#     # Gap checked from 1 -> 9 finally gap of 3 is accepted(as count = 3)
#     for i in range(1, n):
#         if arr[i] - start >= x:
#             start = arr[i]
#             count = count + 1
#         else:
#             continue
#     if count >= K:
#         return True
#     return False


# def aggressive_cows(arr, N, K):
#     ans = 1
#     maxi = 0
#     for i in range(N):
#         maxi = max(maxi, arr[i])
#     for i in range(1, maxi + 1):
#         if(ok(arr, i, K)):
#             ans = i
#         else:
#             break
#     return ans

# # Driver code
# K = 3
# arr = [1, 2, 4, 8, 9]
# N = len(arr)
# ans = aggressive_cows(arr, N, K)
# print(ans)

# Using binary search
# def ok(arr, x, K):
#     n = len(arr)
#     count = 1
#     start = arr[0]
#     for i in range(1, n):
#         if arr[i] - start >= x:
#             start = arr[i]
#             count += 1
#         else:
#             continue
#     if count >= K:
#         return True
#     return False

# def aggressive_cows(arr, N, K):
#     start = 1
#     end = arr[N - 1]
#     ans = -1
#     while end >= start:
#         mid = start + (end - start)//2
#         if ok(arr, mid, K):
#             ans = mid
#             start = mid + 1
#         else:
#             end = mid - 1
#     return ans
# # Driver code
# if __name__ == "__main__":
#     K = 3
#     arr = [1, 2, 4, 8, 9]
#     N = len(arr)
#     print(aggressive_cows(arr, N, K))

# Using binary search and efficient approach
import math
def ok(arr, x, K):
    N = len(arr)
    count = 1
    last = 0
    for i in range(0, N):
        if arr[i] - arr[last] >= x:
            last = i
            count += 1
        if count >= K:
            return True
    return False

def aggressive_cows(arr, N, K):
    start = 0
    end = arr[N - 1] - arr[0]
    ans = -1
    while start <= end:
        mid = start + math.floor((end -start)/2)
        if ok(arr, mid, K):
            ans = mid
            start = mid + 1
        else:
            end = mid - 1
    return ans
# Driver code
K = 3
arr = [1, 2, 4, 8, 9]
N = len(arr)
ans = aggressive_cows(arr, N, K)
print(ans)