# https://practice.geeksforgeeks.org/problems/stickler-theif-1587115621/1?utm_source=gfg&utm_medium=article&utm_campaign=bottom_sticky_on_article


# MENO SOLUTION
def solve(ind, a, dp):
    if ind == 0:
        return a[ind]
    if ind < 0:
        return 0
    if(dp[ind] != -1):
        return dp[ind]
    pick = a[ind]+solve(ind-2, a, dp)
    notpick = solve(ind-1, a, dp)
    dp[ind] = max(pick, notpick)
    return dp[ind]

# Tabulation solution


def solvetabu(ind, a, dp):

    dp[0] = a[0]

    for i in range(1, len(a)):
        pick = a[i]
        if i > 1:
            pick += dp[i-2]
        notPick = 0+dp[i-1]

        dp[i] = max(pick, notPick)

    return dp[len(a)-1]

# space optimization


def solvespace(ind, a):
    prev = 0
    prev2 = 0

    for i in range(0, len(a)):
        pick = a[i]
        if (i > 1):
            pick += prev2
        notpick = 0+prev
        curr = max(pick, notpick)
        prev2 = prev
        prev = curr
    return prev
    '''
    -----------------OR--------------
    prev = 0
    prev2 = 0
    
    for i in range(0,len(a)):
        pick = a[i]
        if (i > 1):
            pick += prev2
        notpick = 0+prev
        curr = max(pick, notpick)
        prev2 = prev
        prev = curr
    return prev
    '''


n = 6
dp = [-1 for i in range(n+1)]
a = [5, 5, 10, 100, 10, 5]
print(solve(n-1, a, dp))
print(solvetabu(n-1, a, dp))
print(solvespace(n, a))
