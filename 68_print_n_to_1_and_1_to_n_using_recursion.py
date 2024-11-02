# Print n to 1 and 1 to n using recursion
def printer(n):
    if n == 0:
        return
    print(n, " ")
    printer(n - 1)
    print(n, " ")


# Driver code
if __name__ == "__main__":
    n = 4
    printer(n)