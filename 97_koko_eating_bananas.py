# # Koko eating bananas
# # Using binary search algo
def check(bananas, mid_val, H):
    time = 0
    for i in range(len(bananas)):
        # in case of a remainder
        if (bananas[i] % mid_val != 0):
            time += bananas[i] // mid_val + 1
        else:
            time += bananas[i] // mid_val
    #  check if time is less than or equals to hour
    if (time <= H):
        return True
    else:
        return False

def minEatingSpeed(piles, H):
    # Fixing the search space
    # as minimum speed of eating must be 1
    start = 1
    # Maximum speed of eating is the maximum bananas in given piles
    end = sorted(piles.copy(), reverse = True)[0]
    while (start < end):
        mid = start + (end - start) // 2
        # Check if the mid is valid
        if (check(piles, mid, H)):
            # if valid continue searching lower search space
            # i.e. koko eats slower
            end = mid
        else:
            # if not valid continue searching higher search space
            # i.e. koko increases the speed
            start = mid + 1
    return end


# Driver code
piles = [30, 11, 23, 4, 20]
H = 6
print(minEatingSpeed(piles, H))

# # Python implementation for the above approach
# def check(bananas, mid_val, H):
#     time = 0;
#     for i in range(len(bananas)):
        
#         # to get the ceil value
#         if (bananas[i] % mid_val != 0):
        
#             # in case of odd number
#             time += bananas[i] // mid_val + 1;
#         else:
        
#             # in case of even number
#             time += bananas[i] // mid_val

#     # check if time is less than
#     # or equals to given hour
#     if (time <= H):
#         return True;
#     else:
#         return False;

# def minEatingSpeed(piles, H):
#     # as minimum speed of eating must be 1
#     start = 1;

#     # Maximum speed of eating
#     # is the maximum bananas in given piles
#     end = sorted(piles.copy(), reverse=True)[0]

#     while (start < end):
#         mid = start + (end - start) // 2;

#         # Check if the mid(hours) is valid
#         if (check(piles, mid, H) == True):
        
#             # If valid continue to search
#             # lower speed
#             end = mid;
#         else:
        
#             # If cant finish bananas in given
#             # hours, then increase the speed
#             start = mid + 1;
#     return end;

# # Driver code
# piles = [30, 11, 23, 4, 20];
# H = 6;
# print(minEatingSpeed(piles, H));

