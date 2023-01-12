

def knapSack_recursive(W, wt, val, n):
    if (n == 0 or W == 0):
        return 0
    if (wt[n-1] <= W):
        return max(val[n-1]+knapSack_recursive(W-wt[n-1], wt, val, n-1), knapSack_recursive(W, wt, val, n-1))
    else:
        return knapSack_recursive(W, wt, val, n-1)


def knapSack_memo(W, wt, val, n):
    dp = [[-1]*(W+1) for i in range(n+1)]
    if (n == 0 or W == 0):
        return 0
    if dp[n][W] != -1:
        return dp[n][W]
    if (wt[n-1] <= W):
        dp[n][W] = max(val[n-1]+knapSack_recursive(W-wt[n-1], wt,
                       val, n-1), knapSack_recursive(W, wt, val, n-1))
    else:
        dp[n][W] = knapSack_recursive(W, wt, val, n-1)
    return dp[n][W]


def kanpSack_Top_Down(W, wt, val, n):
    dp = [[0]*(W+1) for i in range(n+1)]

    for i in range(n+1):
        for j in range(W+1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif wt[i-1] <= j:
                dp[i][j] = max(val[i-1]+dp[i-1][j-wt[i-1]],  dp[i-1][j])
            else:
                dp[i][j] = dp[i-1][j]
    return dp[n][W]


N = 3
W = 4
values = [1, 2, 3]
weight = [4, 5, 1]
print(knapSack_recursive(W, weight, values, N))
print(knapSack_memo(W, weight, values, N))
print(kanpSack_Top_Down(W, weight, values, N))
