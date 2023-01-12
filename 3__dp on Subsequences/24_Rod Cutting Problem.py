# User function Template for python3

class Solution:

    def solveMemo(self, W, wt, val, ind, dp):
        if ind == 0:
            return W*val[0]

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
            dp[0][i] = i*val[0]

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
            prev[i] = i*val[0]
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

    def cutRod(self, price, n):
        length = [i+1 for i in range(n+1)]
        # return self.Unbounded_kanpSack_Top_Down(n, length, price, n)
        dp = [[-1]*(n+1) for i in range(n+1)]
        # return self.solveMemo(n, length, price, n-1, dp)

        # return self.tabulation(n,length,price,n)

        return self.spaceOptimization(n, length, price, n)


# {
 # Driver Code Starts
# Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.cutRod(a, n))

        T -= 1


if __name__ == "__main__":
    main()
# } Driver Code Ends


'''

# this is another way to solve
    def Unbounded_kanpSack_Top_Down(self,W, wt, val, n):
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
'''
