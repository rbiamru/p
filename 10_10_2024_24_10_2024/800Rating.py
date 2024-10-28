# Kosuke Sakurako
# def solve():
#     n = int(input())
#     x = 0
#     c = 1
#     while -n <= x <= n:
#         if c % 2 == 1:
#             x -= 2 * c - 1
#         else:
#             x += 2 * c - 1
#         c += 1
#     if c % 2 == 0:
#         print("Sakurako")
#     else:
#         print("Kosuke")


# for tc in range(int(input())):
#     solve()

####
# Codeforces Round 982 (Div. 2) 
# Problem A Upsolve
# Rectangle
# Import sys module to use for fast input 
import sys
# Set input to read all data at once (useful for competitive programming)
input = sys.stdin.read
def main():
    # Read all input data from the file "input.txt" and split it into a list
    with open("input.txt", "r") as file:
        data = file.read().split()
# Continue processing `data` as input

    # Read all input data at once and split it into a list
    #data = input().split()
    # First element is always the number of test cases
    t = int(data[0])
    # Start index for iterating through data after 't'
    index = 1
    # Initialize a list to store results for each test case
    results = []
    # Loop through each test case
    for _ in range(t):
        # Number of stamps for this case
        n = int(data[index])
        # Initialize maximum width and height as 0
        maxw, maxh = 0, 0
        # Move to the next index for width and height values
        index += 1
        # Loop through each stamp in the test case
        for _ in range(n):
            # Read width and height
            w, h = int(data[index]), int(data[index + 1])
            # Update max width if the current width is larger
            maxw = max(maxw, w)
            # Update max height if the current height is larger
            maxh = max(maxh, h)
            # Move to the next pair of width and height values
            index += 2
        # Calculate perimeter and add to results list as a string
        results.append(str(2 * (maxw + maxh)))
    # Print all results at once, each on a new line
    print("\n".join(results))
# Call the main function
if __name__ == "__main__":
    main()