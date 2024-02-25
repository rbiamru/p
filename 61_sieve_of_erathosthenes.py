# # Sieve of erathosthenes is used to find prime number
def SieveOfEratosthenes(self, N):
        prime = [True for i in range(N+1)]
        p = 2
        li = []
        while p * p <= N:
            if prime[p] == True:
                for i in range(p*p, N+1, p):
                    prime[i] = False
            p += 1
        for p in range(2, N+1):
            if prime[p]:
                li.append(p)
        return li

# Driver code
if __name__ == '__main__':
    n = 20
    print("Prime numbers are:", SieveOfEratosthenes(n))

# # Using 2 for loops
# Primes = [0] * 20
# def SieveOfEratosthenes(n):

#     Primes[0] = 1
#     i = 3
#     while i*i <= n:
#         if Primes[i // 2] == 0:
#             for j in range(3 * i, n+1, 2 * i):
#                 Primes[j // 2] = 1
#         i += 2 

# # Driver code
# if __name__ == '__main__':
#     n = 20
#     SieveOfEratosthenes(n)
#     for i in range(1, n+1):
#         if i == 2:
#             print(i, end="")
#         elif i % 2 == 1 and Primes[i // 2] == 0:
#             print(i, end = " ")