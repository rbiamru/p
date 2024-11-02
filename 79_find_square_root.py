# Find square root
# Using brute force method(Here x is input)
# def floorSqrt(x):
#     # Base case
#     if x == 0 or x == 1:
#         return x
#     i = 1
#     result = 1
#     while result <= x:
#         i += 1
#         result = i * i
#     return i - 1
# # Driver code
# x = 11
# print(floorSqrt(x))
# # Using Binary Search
# def floorSqrt(x):
#     # Base case
#     if x == 0 or x == 1:
#         return x
#     start = 1
#     end = x//2
#     while start <= end:
#         mid = (start + end) // 2
#         if mid * mid == x:
#             return mid
#         elif mid * mid < x:
#             start = mid + 1
#             ans = mid
#         else:
#             end = mid - 1
#     return ans

# # Driver code
# x = 11
# print(floorSqrt(x))
# # Using square root built-in function
# def countSquares(x):
#     sqrt = x ** 0.5
#     result =int(sqrt)
#     return result
# # Driver code
# x = 9
# print(countSquares(x))
# Using exponential
import math
def findSquareRoot(x):
    result = math.exp(math.log(x) / 2)
    floorResult = math.floor(result)
    if floorResult * floorResult == x:
        return floorResult
    else:
        return floorResult
# Driver code
x = 11
print(findSquareRoot(x))