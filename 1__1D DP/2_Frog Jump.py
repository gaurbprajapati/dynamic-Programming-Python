from os import *
from sys import *
from collections import *
from math import *

from typing import *

'''

#recursive solution 

def fun(ind, heights):
    if ind == 0:
        return 0
    left = fun(ind-1, heights)+abs(heights[ind]-heights[ind-1])
    right = 100000000000000000000
    if (ind > 1):
        right = fun(ind-2, heights)+abs(heights[ind]-heights[ind-2])
    return min(left, right)


def frogJump(n: int, heights: List[int]) -> int:
    return fun(n-1, heights)


n = 4
heights = [10, 20, 30, 10]

print(frogJump(n, heights))

'''

'''
#--Memo solution(Top -Down)


def fun(ind,heights,dp):
    if ind==0:
        return 0
    if dp[ind]!=-1:
        return dp[ind]
    left=fun(ind-1,heights,dp)+abs(heights[ind]-heights[ind-1])
    right=100000000000000000000
    if (ind>1):
        right=fun(ind-2,heights,dp)+abs(heights[ind]-heights[ind-2])
    dp[ind]=min(left,right)
    return dp[ind]
  
def frogJump(n: int, heights: List[int]) -> int:
    dp=[-1 for i in range(n+1)]
    return fun(n-1,heights,dp)


n = 4
heights = [10, 20, 30, 10]

print(frogJump(n, heights))

'''


# Tabulation :- (bottom - up) solution

def fun(ind, heights, dp):

    dp[0] = 0
    for i in range(1, ind):
        left = dp[i-1]+abs(heights[i]-heights[i-1])
        right = 10000000000000000
        if (i > 1):
            right = dp[i-2]+abs(heights[i]-heights[i-2])
        dp[i] = min(left, right)

    return dp[ind-1]


def frogJump(n, heights):
    dp = [-1 for i in range(n+1)]

    return fun(n, heights, dp)


n = 4
heights = [10, 20, 30, 10]

print(frogJump(n, heights))


# Space Optimization

def frogJumpspace(ind, height):
    prev = 0
    prev2 = 0
    for i in range(1, ind):
        jumpTwo = 200000000000000
        jumpOne = prev+abs(height[i]-height[i-1])
        if (i > 1):
            jumpTwo = prev2+abs(height[i]-height[i-2])
        curr = min(jumpTwo, jumpOne)

        prev2 = prev
        prev = curr
    return curr


n = 4
heights = [10, 20, 30, 10]

print(frogJumpspace(n, heights))
