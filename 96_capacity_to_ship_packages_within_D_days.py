# Capacity to ship packages within D days
# Using brute force
# def check(v, index, sum, remain, n):
#     # current sum checker for sub array
#     xsum = 0
#     # to check number of days
#     cnt = 0
#     # here we go for all part that are possible.
#     for i in range(index, n):
#         xsum += v[i]
#         if xsum >= sum:
#             if xsum == sum:
#                 xsum = 0
#             else:
#                 xsum = v[i]
#             cnt += 1
#         if n - i == remain - cnt:
#             return 1
#     if xsum != 0:
#         cnt += 1
#     return cnt == remain 

# # Driver code
# vertex = [1, 2, 1]
# d = 2
# m = max(vertex)
# if d == 1:
#     sum = 0
#     for item in vertex:
#         sum += item
#     print(sum)
# else:
#     n = len(vertex)
#     i = 0
#     while True:
#         if check(vertex, i, m, d, n):
#             print("Minimum capacity of boat to ship weights in " + str(d) + "Days should be: " + str(m))
#             break
#         m += 1 

#  Using binary search and greedy algorithm
# Function to check if the weights can be delivered 
# in D days or not
def isValid(weight, n, D, mx):
    # Stores the count of days required to ship all
    # the weights if the maximum capacity is mx or mid
    # days is st
    st = 1 
    # sum of weights is sum
    sum = 0
    # Traverses all the weights
    for i in range(n):
        sum += weight[i]
        # if total weight is more than maximum capacity(restart code)
        if (sum > mx):
            # add days to accommodate the extra ship
            st += 1
            sum = weight[i]
            # if days are more than D, then return false
            if (st > D):
                return False
    return True


# Function to find least weight capacity of a boat
# to ship all weights within D days
def shipWithinDays(weight, D, n):
    #To store total weights
    sum = 0
    # Search space is maximum weight to sum of weights
    # Sum of weights
    for i in range(n):
        sum += weight[i]

    # Maximum weight
    s = weight[0]
    for i in range(1, n):
        s = max(s, weight[i])
    # Store ending value for the search space
    e = sum
    # Store the required result
    res = -1
    # Perform binary search
    while (s <= e):
        #  store the mid value
        mid = s + (e - s) // 2
        # if mid can be shipped, then update the
        # result and end value of the search space
        if (isValid(weight, n, D, mid)):
            res = mid
            e = mid - 1
        # search for minimum value in the right part
        else:
            s = mid + 1

    # Print the result
    print(res)


# Driver C
if __name__ == '__main__':
    weight = [9, 8, 10]
    D = 3
    N = len(weight)
    shipWithinDays(weight, D, N)
              