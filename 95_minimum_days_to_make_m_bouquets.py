# Minimum days to make m bouquets
# # Using brute force method
# # m bouquets with k roses on 'day' day
# def possible(arr, day, m, k):
#     n = len(arr)
#     cnt = 0
#     noOfB = 0
#     for i in range(n):
#         if arr[i] <= day: # Flower blossoms
#             cnt += 1
#         else:
#             noOfB += cnt // k # No. of bouquet calculation
#             cnt = 0
#     noOfB += cnt // k
#     return noOfB >= m

# # m bouquets with k roses
# def roseGarden(arr, k, m):
#     # first validation
#     val = k * m
#     n = len(arr)
#     if val > n:
#         return -1
#     mini = float('inf')
#     maxi = float('-inf')
#     # Defining min and max
#     for i in range(n):
#         mini = min(mini, arr[i])
#         maxi = max(maxi, arr[i])
#     for i in range(mini, maxi + 1):
#         if possible(arr, i, m, k):
#             return i
#     return -1

# # Driver code
# arr = [7, 7, 7, 7, 13, 11, 12, 7]
# k = 3
# m = 2
# ans = roseGarden(arr, k, m)
# if ans == -1:
#     print("We cannot make m bouquets")
# else:
#     print("We can make bouquets on day ", ans)

# Using binary search method
def possible(arr, day, m, k):
    n = len(arr)
    count = 0
    noOfB = 0
    # Count the number of bouquets
    for i in range(n):
        if arr[i] <= day:
            count += 1
        else:
            noOfB += count // k
            count = 0
    noOfB += count // k
    return noOfB >= m

# k roses with m bouquets
def roseGarden(arr, k, m):
    val = m * k # m bouquets with k roses
    n = len(arr)
    if val > n:
        return -1
    mini = float('inf')
    maxi = float('-inf')
    for i in range(n):
        mini = min(mini, arr[i])
        maxi = max(maxi, arr[i])
    # Apply binary search
    start = mini
    end = maxi
    while start <= end:
        mid = (start + end)//2
        if possible(arr, mid, m, k):
            end = mid - 1
        else:
            start = mid + 1
    return start


# Driver code
arr = [7, 7, 7, 7, 13, 11, 12, 7]
k = 3 # 3 roses
m = 2 # 2bouquets
ans = roseGarden(arr, k, m)
if ans == -1:
    print("We cannot make m bouquets")
else:
    print("We can make bouquets on day", ans)