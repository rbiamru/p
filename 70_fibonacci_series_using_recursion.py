# # Using logic illa magic brute force method
# def nthFibonacci(self, n : int) -> int:
#     # code here
#     a=0
#     b=1
#     mod=1000000007
#     for i in range(1,n):
#         c=(a+b)%mod   #swap here
#         a=b
#         b=c
#     return c


# # Using brute force method
# def fibonacci(n):
    # a = 0
    # b = 1
    # if n == 0:
    #     return 0
    # elif n == 1:
    #     return 1
    # elif n > 1:
    #     for i in range(2, n + 1):
    #         c = a + b
    #         a = b
    #         b = c
    #     return c
#     while n < 0:
#         print("Wrong input")
#         n = input("Try again")

# # Driver code
# print(fibonacci(9))
# # Using recursion
# def fibonacci(n):
#     if n <= 1:
#         return n
#     return fibonacci(n - 1) + fibonacci(n - 2)
# # Driver code
# print(fibonacci(9))
# # Using dynamic programming nothing but using database
# def fibonacci(n):
#     f = [0, 1]
#     for i in range(2, n + 1):
#         f.append(f[i - 1] + f[i - 2])
#     return f[n]
# # Driver code
# print(fibonacci(9))
# Using matrix
def fib(n):
    F = [[1, 1],
         [1, 0]]
    if n == 0:
        return 0
    power(F, n - 1)
    return F[0][0]

def multiply(F, M):
    x = (F[0][0] * M[0][0] + F[0][1] * F[1][0])
    y = (F[0][0] * M[0][1] + F[0][1] * M[1][1])
    z = (F[1][0] * M[0][0] + F[1][1] * M[1][0])
    w = (F[1][0] * M[0][1] + F[1][1] * M[1][1])
    F[0][0] = x
    F[0][1] = y
    F[1][0] = z
    F[1][1] = w

def power(F, n):
    if(n == 0 or n == 1):
        return
    M = [[1, 1], 
         [1, 0]]
    power(F, n // 2)
    multiply(F, F)
    if n % 2 != 0:
        multiply(F, M)

# Driver code
if __name__ == "__main__":
    n = 9
    print(fib(n))