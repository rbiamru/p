#Maximum product subarray
#********Using Brute Force Method
# def maxSubarrayProduct(arr, n):
#     result = arr[0]
#     for i in range(n):
#         mul = arr[i]
#         for j in range(i + 1, n):
#             result = max(result, mul)
#             mul *= arr[j]
#         result = max(result, mul)
#     return result

# #Driver code
# if __name__ == '__main__':
#     arr = [1, -2, -3, 0, 7, -8, -2]
#     n = len(arr)
#     print("Maximum sub array product is", maxSubarrayProduct(arr, n))

# #***********Using Kadane's Algorithm
def maxSubarrayProduct(arr, n):
    max_ending_here = arr[0]
    min_ending_here =  arr[0]
    max_so_far = arr[0]
    for i in range(1, n):
        temp = max(max(arr[i], arr[i]*min_ending_here), arr[i]*max_ending_here)
        min_ending_here = min(min(arr[i], arr[i]*max_ending_here), arr[i]*min_ending_here)
        max_ending_here = temp
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far
# #Driver code
# arr = [1, -2, -3, 0, 7, -8, -2]
# n = len(arr)
# print(f"Maximum sub array product is {maxSubarrayProduct(arr,n)}")

#*****Using traversal from starting and end
# def maxSubarrayProduct(arr, n):
#     ans = float('-inf')
#     product = 1
#     for i in range(n):
#         product *= arr[i]
#         ans = max(ans, product)
#         if arr[i] == 0:
#             product = 1
#     product = 1
#     for i in range( n-1, -1, -1):
#         product *= arr[i]
#         ans = max(ans, product)
#         if arr[i] == 0:
#             product = 1
#     return ans
## Driver code
# if __name__ == '__main__':
#     arr = [1, -2, -3, 0, 7, -8, -2]
#     n = len(arr)
#     print("Maxiumum Subarray product is", maxSubarrayProduct(arr, n))