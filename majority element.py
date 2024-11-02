# Function to find majority element in an array
## Brute Force method
# def findMajority(arr, n):
#     maxCount = 0
#     index = -1 # Sentinels
#     for i in range(n):
#         count = 1
#         # We compare the element in ith position with i+1th position
#         for j in range(i+1, n):
#             if arr[i] == arr[j]:
#                 count += 1
#         # Update maxCount if count of current element is greater
#         if count > maxCount:
#             maxCount = count
#             index = i
#     # if maxCount is greater than n/2 return the corresponding element
#     if maxCount > n//2:
#         return arr[index]
#     else:
#         return "no majority element"

##***** Using Binary Search Tree
# #class for creating node
# class Node():
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None
#         self.count = 1 # No. of times the same number has been added in the node
    
# class BST():
#     def __init__(self):
#         self.root = None
#     def insert(self, data, n):
#         out = None
#         if self.root == None:
#             self.root = Node(data)
#         else:
#             out = self.insertNode(self.root, data, n)
#         return out
#     def insertNode(self, currentNode, data, n):
#         if currentNode.data == data:
#             currentNode.count += 1
#             if currentNode.count > n//2:
#                 return currentNode.data
#             else:
#                 return None
#         elif currentNode.data < data:
#             if currentNode.right:
#                 self.insertNode(currentNode.right, data, n)
#             else:
#                 currentNode.right = Node(data)
#         elif currentNode.data > data:
#             if currentNode.left:
#                 self.insertNode(currentNode.left, data, n)
#             else:
#                 currentNode.left = Node(data)
# # Driver code for tree
# arr = [3, 2, 3]
# n = len(arr)

# # declaring none tree
# tree = BST()
# flag = 0
# for i in range(n):
#     out = tree.insert(arr[i], n)
#     if out != None:
#         print(arr[i])
#         flag = 1
#         break
# if flag == 0:
#     print("No majority element")
# def findCandidate(arr):
#     maj_index = 0
#     count = 1
#     for i in range(len(arr)):
#         if arr[maj_index] == arr[i]:
#             count += 1
#         else:
#             count -= 1
#         if count == 0:
#             maj_index = i
#             count = 1
#     return arr[maj_index]
# def isMajority(arr, cand):
#     count = 0
#     for i in range(len(arr)):
#         if arr[i] == cand:
#             count += 1
#     if count > len(arr)/2:
#         return True
#     else:
#         return False

    
# def printMajority(arr):
# # Find the candidate for majority
#     cand = findCandidate(arr)
#     # Print the candidate if it is majority
#     if isMajority(arr, cand) == True:
#         print(cand)
#     else:
#         print("No majority element")
# # Driver code
# arr = [1, 3, 3, 1, 2]
# printMajority(arr)
# def findMajority(arr, n):
#     dict = {}
#     for i in range(n):
#         if arr[i] in dict:
#             dict[arr[i]] += 1
#         else:
#             dict[arr[i]] = 1
#     is_majority_present = False
#     for key in dict:
#         if dict[key] > n/2:
#             is_majority_present = True
#             return key
#             break
#     if not is_majority_present:
#         return "No majority element"
# *****Using sorting
def findMajority(arr, n):
    # sort the array in O(nlogn)
    arr.sort()
    count, max_ele, temp, f = 1, -1, arr[0], 0
    for i in range(1, n):
        #increases the count if the same element occurs otherwise starts counting new element
        if temp == arr[i]:
            count += 1
        else:
            count = 1
            temp = arr[i]
        #sets maximum count and stores maximum occurred element so far if maximum count becomes > n/2 it breaks out setting the flag
        if max_ele < count:
            max_ele = count
            ele = arr[i]
            if max_ele > n//2:
                f = 1
                break
    #returns maximum occurred element if there is no such element it returns -1
    if f == 1:
        return ele
    else:
        return -1    
# Using recursion
# def count_occurrences(arr, num):
#     count = 0
#     for i in arr:
#         if i == num:
#             count += 1
#     return count
# def findMajorityUtil(arr, low, high):
#     if low == high:
#         return arr[low]
#     mid = (low + high)//2
#     left_majority = findMajorityUtil(arr, low, mid)
#     right_majority = findMajorityUtil(arr, mid+1, high)
#     if left_majority == right_majority:
#         return left_majority
#     left_count = count_occurrences(arr[low:high+1], left_majority)
#     right_count = count_occurrences(arr[low:high+1], right_majority)
#     if left_count > (high-low+1) // 2:
#         return left_majority
#     if right_count > (high - low + 1)//2:
#         return right_majority
#     return -1
# def findMajority(arr, n):
#     majority = findMajorityUtil(arr, 0, n-1)
#     if majority != -1:
#         return majority
#     else:
#         return "No majority element"         
# Driver code
if __name__ == "__main__":
    arr = [1, 1, 2, 1, 3, 5, 1]
    n = len(arr)
    # Function calling
    print(findMajority(arr, n))
