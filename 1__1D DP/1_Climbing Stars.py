

'''

You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps


'''

# tabulation solution


def climbStairs(n: int):
    dp = [-1 for i in range(n+1)]
    dp[0] = 1
    dp[1] = 1
    for i in range(2, n+1):
        dp[i] = dp[i-1]+dp[i-2]

    return dp[n]


n = 2
print(climbStairs(n))

# Space Optimization


def climbStairs(n: int):
    prev2 = 1
    prev1 = 1
    for i in range(2, n+1):
        curr = prev2+prev1
        prev2 = prev1
        prev1 = curr

    return prev1


n = 2
print(climbStairs(n))
