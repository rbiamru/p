# Using logic illa brute force method
def power(self,N,R):
        #Your code here
        MOD = 10**9 + 7
        result = pow(N, R, MOD)
        return result 

# # Using brute force method
# def pow(x, n):
#     power = 1
#     for i in range(0, n):
#         power = power * x
#     return power
# # Driver code
# if __name__ == "__main__":
#     x = 2
#     n = 3
#     print(pow(x, n))
# # Using recursion
# def power(x, n):
#     if (n == 0):
#         return 1
#     if (x == 0):
#         return 0
#     return x * power(x, n - 1)
# # Driver code
# if __name__ == "__main__":
#     x = 2
#     n = 3
#     print(power(x, n))
# # Using Divide and conquer approach
# def power(x, y):
#     if y == 0:
#         return 1
#     elif int(y % 2) == 0:
#         return power(x, int(y / 2)) * power(x, int(y / 2))
#     else:
#         return x * power(x, int(y / 2)) * power(x, int(y / 2))
# # Driver code
# if __name__ == "__main__":
#     x = 2
#     y = 3
#     print(power(x, y))
# # Using Divide and conquer approach in an optimised way
# def power(x, y):
#     temp = 0
#     if y == 0:
#         return 1
#     temp = power(x, y//2)
#     if y % 2 == 0:
#         return temp * temp
#     else:
#         return x * temp * temp
# if __name__ == "__main__":
#     x = 2
#     y = 3
#     print(power(x, y))
# Using optimised divide and conquer approach and an extended version 
# for covering float x and negative y
# def power(x, y):
#     if y == 0:
#         return 1
#     temp = power(x, int(y/2))
#     if y % 2 == 0:
#         return temp * temp
#     else:
#         if y > 0:
#             return x * temp * temp
#         else:
#             return (temp * temp )/ x

# if __name__ == "__main__":
#     x, y = 2, -3
#     print('%0.6f' %(power(x, y)))
# #*************** Using inbuilt pow function
# def power(x, n):
#     return pow(x, n)
# # Driver code
# if __name__ == "__main__":
#     x = 2
#     n = 3
#     print(power(x, n))
# # Using binary operators
# def power(x, n):
#     result = 1
#     while(n > 0):
#         if n % 2 == 0:
#             x = x * x
#             n = n / 2
#         else:
#             result = result * x
#             n = n -1
#     return result
# # Driver code
            
# if __name__ == "__main__":
#     x = 2
#     n = 3
#     print(power(x, n))
# #***********Using ** operator
# def power(x, n):
#     return x ** n
# # Driver code
# if __name__ == "__main__":
#     x = 2
#     n = 3
#     print(power(x, n))
# #***********Using numpy module
# import numpy as np
# N = 2
# X = 3
# result = np.power(N, X)
# print(result)
# #********** Using math.log2()
# import math
# def calculatePower(a, n):
#     return round(2 ** (math.log2(a) * n))
# # Driver code
# if __name__ == "__main__":
#     a = 2
#     n = 3
#     print(calculatePower(a, n))
# #****** using  math.log()
# import math
# def calculatePower(x, n):
#     ans = math.exp(math.log(x)*n)
#     ans = round(ans)
#     return ans
# # Driver code
# if __name__ == "__main__":
#     x = 2
#     n = 3
#     print(calculatePower(x, n))