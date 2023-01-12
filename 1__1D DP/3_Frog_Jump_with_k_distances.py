# Tabulation :- (bottom - up) solution

def fun(ind, heights, dp, k):

    dp[0] = 0
    for i in range(1, ind):

        minStep = 100000000000000000000000
        for j in range(1, k+1):
            if (i-j >= 0):
                jump = dp[i-j]+abs(heights[i]-heights[i-j])

            minStep = min(minStep, jump)
        dp[i] = minStep
    return dp[ind-1]


def frogJump(n, heights, k):
    dp = [-1 for i in range(n+1)]

    return fun(n, heights, dp, k)


n = 6
k = 2
heights = [30, 10, 60, 10, 60, 50]

print(frogJump(n, heights, k))
