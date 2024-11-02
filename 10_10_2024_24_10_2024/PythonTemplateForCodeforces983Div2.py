# A problem
# Switches and light
# Defines a class named Solution to hold test information and methods.
class Solution: 
    # Indicates that there may be multiple cases
    hasMultipleCases = True
    # Initializes n, representing the number of elements in the list, to None.
    n: int = None
    # Initializes a representing the list of integers, to None.
    a: list = None

    @classmethod
    # Preprocess method (empty), can be used for any setup before input handling.
    def preprocess(cls):
        pass

    @classmethod
    # Method to handle input for each test case.
    def input(cls, testcase):
        # Reads the integer input and assigns it to n.
        cls.n = int(input())
        # Reads the list of integers and assigns it to a.
        cls.a = list(map(int, input().split()))

    @classmethod
    # Method to solve the problem for the current test case.
    def solve(cls, testcase):
        # Counts the number of 1s by summing elements in list a.
        cnt0 = sum(cls.a)
        # Print results:
        # `cnt0 & 1`: Checks if the count of 1s is odd (1 if odd, 0 if even)
        # `min(cnt0, cls.n * 2 - ctn0)`: Minimum value between count of 1s and twice the list length minus cnt0
        print(cnt0 & 1, min(cnt0, cls.n * 2 - cnt0))

############ WARNING: Written only for VS code not on codeforces
    # Main function to loop over multiple test cases
if __name__ == "__main__":
    ### For using input1.txt file in the compile time
    # Bash command: 
    # $ python PythonTemplateForCodeforces983Div2.py < input1.txt
    t = int(input().strip())
    for i in range(1, t + 1):
        Solution.input(i)
        Solution.solve(i)
       
    ### For copy pasting inputs now in the runtime
    # Click the arrow on top right corner
    # t = int(input("Enter number of test cases: "))
    # for i in range(1, t + 1):
    #     Solution.input(i)
    #     Solution.solve(i)

