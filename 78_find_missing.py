# Find missing number in a series
# # Using Hashing method
# def findMissing(arr, N):
#     arr
#     temp = [0] * (N + 1)
#     for i in range(0, N):
#         temp[arr[i] - 1] = 1
#     for i in range(0, N + 1):
#         if temp[i] == 0:
#             ans = i + 1
#     print(ans)

# # Driver code
# if __name__ == "__main__":
#     arr = [1, 2, 3, 5]
#     N = len(arr)
#     findMissing(arr, N)
# # Using n * (n + 1) / 2
# def getMissingNo(arr, N):
#     total = (N + 1) * (N + 2)//2
#     sum_of_arr = sum(arr)
#     return total - sum_of_arr
# if __name__ == "__main__":
#     arr = [1, 2, 3, 5]
#     N = len(arr)
#     miss = getMissingNo(arr, N)
#     print(miss)
# #***********Using modification of overflow
# def getMissingNo(arr, n):
#     i, total = 0, 1
#     for i in range(2, n + 2):
#         total += i
#         total -= arr[i - 2]
#     return total
# # Driver code
# if __name__ == "__main__":
#     arr = [1, 2, 3, 5]
#     N = len(arr)
#     print(getMissingNo(arr, N))
# #*************Using XOR
# def getMissingNo(arr, n):
#     x1 = arr[0]
#     x2 = 1
#     for i in range(1, n):
#         x1 = x1 ^ arr[i]
#     for i in range(2, n + 2):
#         x2 = x2 ^ i
#     return x1 ^ x2
# # Driver program
# if __name__ == "__main__":
#     arr = [1, 2, 3, 5]
#     N = len(arr)
#     miss = getMissingNo(arr, N)
#     print(miss)
# # ************Using cyclic sort
# def getMissingNo(arr, n):
#     i = 0
#     while i < n:
#         correctpos = arr[i] - 1
#         if arr[i] < n and arr[i] != arr[correctpos]:
#             arr[i], arr[correctpos] = arr[correctpos], arr[i]
#         else:
#             i += 1
#     for index in range(n):
#         if arr[index] != index + 1:
#             return index + 1
#     return n
# # Driver code
# if __name__ == "__main__":
#     arr = [1, 2, 3, 5]
#     N = len(arr)
#     print(getMissingNo(arr, N))
#************Using negative
def findMissing(arr, n):
    for i in range(0, n):
        if abs(arr[i]) - 1 == n:
            continue
        ind = abs(arr[i]) - 1
        arr[ind] *= -1
    ans = n + 1
    for i in range(0, n):
        if arr[i] > 0:
            ans = i + 1
    print(ans)

# Driver code
if __name__ == "__main__":
    arr = [1, 3, 7, 5, 6, 2]
    n = len(arr)
    findMissing(arr, n)