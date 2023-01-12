

# User function Template for python3

class Solution:

    def solveMemo(self, W, wt, val, ind, dp):
        if ind == 0:
            return (W//wt[0]) * val[0]

        if (dp[ind][W] != -1):
            return dp[ind][W]

        notpick = 0+self.solveMemo(W, wt, val, ind-1, dp)

        pick = -float('inf')

        if (W >= wt[ind]):
            pick = val[ind]+self.solveMemo(W-wt[ind], wt, val, ind, dp)

        dp[ind][W] = max(pick, notpick)

        return dp[ind][W]

    def tabulation(self, W, wt, val, n):
        dp = [[0]*(W+1) for i in range(n+1)]
        for i in range(wt[0], W+1):
            dp[0][i] = int(i/wt[0]) * val[0]

        for ind in range(1, n):
            for cap in range(0, W+1):
                notTaken = 0 + dp[ind-1][cap]

                taken = -float('inf')
                if(wt[ind] <= cap):
                    taken = val[ind] + dp[ind][cap - wt[ind]]

                dp[ind][cap] = max(notTaken, taken)

        return dp[n-1][W]

    def spaceOptimization(self, W, wt, val, n):
        prev = [0 for i in range(W+1)]

        for i in range(wt[0], W+1):
            prev[i] = int(i/wt[0]) * val[0]
        for ind in range(1, n):
            curr = [0 for i in range(W+1)]
            for cap in range(0, W+1):
                notTaken = 0 + prev[cap]

                taken = -float('inf')
                if(wt[ind] <= cap):
                    taken = val[ind] + curr[cap - wt[ind]]
                curr[cap] = max(notTaken, taken)
            prev = curr
        return prev[W]

    def knapSack(self, N, W, val, wt):

        dp = [[-1]*(W+1) for i in range(N+1)]

        return self.solveMemo(W, wt, val, N-1, dp)
        # return self.tabulation( W, wt, val, N)

        # return self.spaceOptimization(W, wt, val, N)
        # code here


N = 4
W = 8
va = [1, 4, 5, 7]
wt = [1, 3, 4, 5]
dp = [[-1]*(W+1) for i in range(N+1)]

ob = Solution()

print(ob.solveMemo(W, wt, va, N-1, dp))
print(ob.tabulation(W, wt, va, N))
print(ob.spaceOptimization(W, wt, va, N))


'''

this is other way to solve
def Unbounded_kanpSack_Top_Down(W, wt, val, n):
    dp = [[0]*(W+1) for i in range(n+1)]

    for i in range(n+1):
        for j in range(W+1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif wt[i-1] <= j:
                dp[i][j] = max(val[i-1]+dp[i][j-wt[i-1]],  dp[i-1][j])
            else:
                dp[i][j] = dp[i-1][j]
    return dp[n][W]
# } Driver Code Ends

'''
