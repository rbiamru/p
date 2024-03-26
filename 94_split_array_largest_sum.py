# Split array for getting maximum sum of all sub arrays is minimum
# # Using naive approach or backtracking

# ans = 10 ** 7
# def solve(a, n, k, index, sum, maxsum):
    global ans
    # K = 1 is the base case
    if k == 1:
        maxsum = max(maxsum, sum)
        sum = 0
        for i in range(index, n):
            sum += a[i]
        # We update maxsum            
        maxsum = max(maxsum, sum)
        # the answer is stored in ans
        ans = min(ans, maxsum)
        return
    sum = 0
    # Using for loop to divide the array into k-subarray
    for i in range(index, n):
        sum += a[i]
        maxsum = max(maxsum, sum)
        solve(a, n, k - 1, i + 1, sum, maxsum)
# # Using driver code
# arr = [1, 2, 3, 4]
# k = 3 
# n = 4
# solve(arr, n, k, 0, 0, 0)
# print(ans)

# Using binary search
def check(mid, array, n, K):
    count = 0
    sum = 0
    for i in range(n):
        if array[i] > mid:
            return False
        sum += array[i]
        if sum > mid:
            count += 1
            sum = array[i]
    count += 1
    if count <= K:
        return True
    return False

def solve(array, n, K):
    start = max(array)
    end = 0
    for i in range(n):
        end += array[i]
    answer = 0
    while start <= end:
        mid = (start + end)// 2
        if check(mid, array, n, K):
            answer = mid
            end = mid - 1
        else:
            start = mid + 1
    return answer
# Driver code
if __name__ == "__main__":
    array = [1, 2, 3, 4]
    n = len(array)
    K = 3
    print(solve(array, n, K))