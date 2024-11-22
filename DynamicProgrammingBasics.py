# Frog Jump 
# Problem Link: https://www.naukri.com/code360/problems/frog-jump_3621012?source=youtube&campaign=striver_dp_videos&utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_dp_videos&leftPanelTabValue=PROBLEM
from os import *
from sys import *
from collections import *
from math import *

from typing import *
import sys
  
def frogJump(n: int, heights: List[int]) -> int:
# 1) All possibilities or All Ways (recursion)
# Recursion converted to Dynamic Programming === Reverse Engineering
# Moving from f(n)
#      f(n - 1)  f(n - 2) (1 step jump Analepsis or Protagonist) (2 step jump A or P)
# f(n) means energy required to jump from n to 1st step (Analepsis or Protagonist)
# f(1) means energy required to jump from 1st step to 1st step (A or P) = 0
# f(ith step) ith step or parameter
    if n == 1: # Base case i.e. jump from 1 -> 1
        return 0
    left_branch = frogJump(n - 1, heights) + abs(heights[n - 1] - heights[n - 2])
    right_branch = int(sys.maxsize)
    if n > 2: # if n == 2 frog will be in the 0th step which is not there
        right_branch = frogJump(n - 2, heights) + abs(heights[n - 1] - heights[n - 3])
    return min(left_branch, right_branch)
# 2) Memoization (O SP -> Overlapping Sub-Problem) Overlapping == Old
# Using Memoization: O SP (overlapping or old or remember old) (SubProblems)
# def frogJump(n: int, heights: List[int]) -> int:
#     if n == 1: # Base case i.e. jump from 1 -> 1
#         return 0
#     dp = [-1] * (n + 1) # "n + 1" sub-problems
#     if dp[n] != -1: return dp[n] # "O -> Overlapping or Old or remember old f()s"
#     left_branch = frogJump(n - 1, heights) + abs(heights[n - 1] - heights[n - 2])
#     right_branch = int(sys.maxsize)
#     if n > 2: # if n == 2 frog will be in the 0th step which is not there
#         right_branch = frogJump(n - 2, heights) + abs(heights[n - 1] - heights[n - 3])
#     dp[n] = min(left_branch, right_branch)
#     return dp[n]
# 3) Using Tabulation: SP + recurrences with ongoing prev2, prev, curri 
def frogJump(n: int, heights: List[int]) -> int:
    dp = [-1] * (n + 1) # "n + 1" SubProblems
    # Recurrences (base case, from 2nd step to nth step)
    dp[1] = 0
    for i in range(2, n + 1):
        left_branch = dp[i - 1] + abs(heights[i - 1] - heights[i - 2])
        right_branch = int(sys.maxsize)
        if i > 2:
            right_branch = dp[i - 2] + abs(heights[i - 1] - heights[i - 3])
        dp[i] = min(left_branch, right_branch)
    return dp[n]

# 4) Using Optimised Approach: Tabulation (with ongoing prev2, prev, curri)
# prev2     prev   curri
#           prev2   prev    curri
#                   prev2   prev  curri
# dp[i-2] dp[i-1] dp[i] 

