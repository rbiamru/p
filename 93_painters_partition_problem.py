# Painters partition problem
# Working solution
class Solution:
    def minTime (self, arr, n, k):
        if k == 1:   # If there is only one painter then time taken will be the total units.
            return sum(arr)
        if n <= k:   # If no. of boards is less than or equal to the no. of painters then min time required will be the length of the longest board
            return max(arr)
    
        def isPossible(maxTime):  # Function to check if its possible for the painters to finish the work in 'maxTime'.
            count = 1
            total = 0
            for i in arr:
                if total + i > maxTime:
                    count += 1
                    if count > k or i > maxTime:
                        return False
                    total = i
                else:
                    total += i
            return True
    
        left = 0
        right = sum(arr)   # because time taken can't be greater than the total units.
        result = -1
        while left <= right:
            mid = left + (right - left) // 2
            if isPossible(mid):
                right = mid - 1   # If possible we check, if its possible to do the work in less time.
                result = mid
            else:
                left = mid + 1   # If not possible then it means that the time taken must be greater than mid.
        return result

# # Using dynamic programming
# def sum(arr, frm, to):
#     total = 0
#     for i in range(frm, to + 1):
#         total += arr[i]
#     return total
# def partition(arr, n, k):
#     if k == 1:
#         return sum(arr, 0, n -1)
#     if n == 1:
#         return arr[0]
#     best = 10 ** 9
#     for i in range(1, n + 1):
#         best = min(best, max(partition(arr, i, k - 1), sum(arr, i, n - 1)))
#     return best

# # Driver code
# arr = [10, 20, 60, 50, 30, 40]
# n = len(arr)
# k = 3 # No. of painters
# print(partition(arr, n, k))

# # Using bottom-up memoization method
# def sum(arr, start, to):
#     total = 0
#     for i in range(start, to + 1):
#         total += arr[i]
#     return total
# def findMax(arr, n, k):
#     dp = [[0 for i in range(n + 1)]
#           for j in range(k + 1)]
#     for i in range(1, n + 1):
#         dp[1][i] = sum(arr, 0, i - 1)
#     for i in range(1, k + 1):
#         dp[i][1] = arr[0]
#     for i in range(2, k + 1):
#         for j in range(2, n + 1):
#             best = 10**9
#             for p in range(1, j + 1):
#                 best = min(best, max(dp[i - 1][p], sum(arr, p, j - 1)))
#             dp[i][j] = best
#     return dp[k][n]
# # Driver code
# arr = [10, 20, 60, 50, 30, 40]
# n = len(arr)
# k = 3
# print(findMax(arr, n, k))