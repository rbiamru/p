# # Merge overlapping intervals using sorting
# def mergeIntervals(intervals):
#     #Sort the array
#     intervals.sort()
#     stack = []
#     stack.append(intervals[0])
#     # How to remember this
#     for i in intervals[1:]:
#         if stack[-1][0] <= i[0] <= stack[-1][-1]:
#             stack[-1][-1] = max(stack[-1][-1], i[-1])
#         else:
#             stack.append(i)
#     for i in range(len(stack)):
#         print(stack[i])

# #Driver code
# if __name__ == '__main__':
#     arr = [[6, 8], [1, 9], [2, 4], [4, 7]]
#     mergeIntervals(arr)
# Merge overlapping intervals using sorting
# O(n log n) time and O(1) extra space
def mergeIntervals(arr, n):
    # Sort in ascending order
    arr.sort(key = lambda x: x[0])
    index = 0
    for i in range(1, n):
        if arr[index][1] >= arr[i][0]:
            arr[index][1] = max(arr[index][1], arr[i][1])
        else:
            index = index + 1
            arr[index] = arr[i]
    print("The merged intervals are:")
    for i in range(index + 1):
        print(arr[i])

#Driver code
if __name__ == '__main__':
    arr = [[1, 3], [2, 4], [6, 8], [9, 10]]
    n = len(arr)
    mergeIntervals(arr, n)
    