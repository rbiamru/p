# Using GPT converted to integer
def atoi(self, s):
        num = 0
        sign = 1
        i = 0
        
        # Handle leading whitespace
        while i < len(s) and s[i] == ' ':
            i += 1
        
        # Handle sign
        if i < len(s) and (s[i] == '+' or s[i] == '-'):
            sign = -1 if s[i] == '-' else 1
            i += 1
        
        # Convert remaining digits
        while i < len(s) and s[i].isdigit():
            num = num * 10 + int(s[i])
            i += 1
        
        # Check if there are non-numeric characters remaining
        while i < len(s) and not s[i].isdigit():
            return -1
        
# Atoi i.e. convert int.Parse or type casting in python using recursion
def myAtoiRecursive(string, num):
    if string.isalpha():
        return 0
    if len(string) == 0:
        return 0
    if len(string) == 1:
        return int(string[0: 1]) + num * 10
    num = int(string[0: 1]) + num * 10
    return myAtoiRecursive(string[1:], num)
# Driver code
string = "112"
print(myAtoiRecursive(string, 0))
