# User function Template for python3

class Solution:

    def solveMemo(self, W, wt, val, ind, dp):
        if ind == 0:
            if (wt[0] <= W):
                return val[0]
            else:
                return 0

        if (dp[ind][W] != -1):
            return dp[ind][W]

        notpick = 0+self.solveMemo(W, wt, val, ind-1, dp)

        pick = -float('inf')

        if (W >= wt[ind]):
            pick = val[ind]+self.solveMemo(W-wt[ind], wt, val, ind-1, dp)

        dp[ind][W] = max(pick, notpick)

        return dp[ind][W]

    def tabulation(self, W, wt, val, n):
        dp = [[0]*(W+1) for i in range(n+1)]
        for i in range(wt[0], W+1):
            dp[0][i] = val[0]
        for ind in range(1, n):
            for cap in range(0, W+1):
                notTaken = 0 + dp[ind-1][cap]

                taken = -float('inf')
                if(wt[ind] <= cap):
                    taken = val[ind] + dp[ind-1][cap - wt[ind]]

                dp[ind][cap] = max(notTaken, taken)

        return dp[n-1][W]

    def spaceOptimization(self, W, wt, val, n):
        prev = [0 for i in range(W+1)]

        for i in range(wt[0], W+1):
            prev[i] = val[0]
        for ind in range(1, n):
            curr = [0 for i in range(W+1)]
            for cap in range(0, W+1):
                notTaken = 0 + prev[cap]

                taken = -float('inf')
                if(wt[ind] <= cap):
                    taken = val[ind] + prev[cap - wt[ind]]
                curr[cap] = max(notTaken, taken)
            prev = curr
        return prev[W]

    def spaceOptimizationInoneCol(self, W, wt, val, n):
        prev = [0 for i in range(W+1)]

        for i in range(wt[0], W+1):
            prev[i] = val[0]

        for i in range(wt[0], W+1):
            prev[i] = val[0]
        for ind in range(1, n):
            for cap in range(W, -1, -1):
                notTaken = 0 + prev[cap]

                taken = -float('inf')
                if(wt[ind] <= cap):
                    taken = val[ind] + prev[cap - wt[ind]]
                prev[cap] = max(notTaken, taken)
            # prev=curr
        return prev[W]

    # Function to return max value that can be put in knapsack of capacity W.
    def knapSack(self, W, wt, val, n):
        dp = [[-1]*(W+2) for i in range(n+1)]
        # return self.solveMemo(W, wt, val, n-1,dp)
        # return self.tabulation(W, wt, val, n)\
        # return self.spaceOptimization(W, wt, val, n)
        return self.spaceOptimizationInoneCol(W, wt, val, n)


N = 3
W = 4
values = [1, 2, 3]
weight = [4, 5, 1]
dp = [[-1]*(W+2) for i in range(N+1)]
ob = Solution()
print(ob.tabulation(W, weight, values, N))
print(ob.solveMemo(W, weight, values, N-1, dp))
print(ob.spaceOptimization(W, weight, values, N))
print(ob.spaceOptimizationInoneCol(W, weight, values, N))
