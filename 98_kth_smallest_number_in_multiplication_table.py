# Kth smallest number in multiplication table
# Naive approach
# class Solution:
#     def findKthNumber(self, m, n, k):
#         res = []
#         for i in range(1, m + 1):
#             for j in range(1, n + 1):
#                 res.append(i * j)
#         res.sort()
#         return res[k - 1]

# # Driver code
# m, n = 3, 3
# k = 5
# res = Solution()
# print(res.findKthNumber(m, n, k))

#  Using Min Heap approach
# import heapq
# class Solution:
#     def findKthNumber(m, n, k):
#         pq = []
#         # Nested loops
#         for i in range(1, m + 1):
#             for j in range(1, n + 1):
#                 val = i * j
#                 # 2 conditions are checked(length of pq, val greater than first element in heap)
#                 if len(pq) == k:
#                     if val*-1 > pq[0]:
#                         heapq.heappop(pq)
#                         heapq.heappush(pq, val*-1)
#                     else:
#                         continue
#                 else:
#                     heapq.heappush(pq, val*-1)
#             return pq[0]*-1
# # Driver code
# m, n = 3, 3
# k = 5
# res = Solution()
# print(res.findKthNumber(m, n, k))

# Using Binary search algorithm
class Solution:
    def findKthNumber(self, m, n, k):
        def count(m, n, val):
            cnt = 0
            for i in range(1, m + 1):
                cnt += min( val // i, n)
            return cnt


        # Search space
        l, h = 1, m * n
        while l < h:
            mid = (l + h)//2
            if (count(m, n, mid) < k):
                l = mid + 1
            else:
                h = mid
        return l

# Driver code
m, n = 3, 3
k = 5
res = Solution()
print(res.findKthNumber(m, n, k))


