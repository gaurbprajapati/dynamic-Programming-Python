class Solution:
    def minDifference(self, arr, n):
		def subsetsumproblem(n, arr, sum, dp):
            for i in range (n+1):
                for j in range (sum+1):
                    if i==0 and j==0:
                        dp[i][j]=True
                    elif i==0:
                        dp[i][j]=False
                    elif j==0:
                        dp[i][j]=True
                    
                    elif (arr[i-1]<=j):
                        dp[i][j]=(dp[i-1][j] or dp[i-1][j-arr[i-1]])
                    
                    elif (arr[i-1]>j):
                        dp[i][j]=dp[i-1][j]
            return dp
        rng = sum(arr)
        dp =[[False for i in range(rng + 1)] for j in range(n + 1)]
        subsetsumproblem( n, arr, rng ,dp  )
        diff = 1000000000000000000000000
        
        # for i in range (n+1):
        for j in range (rng//2,-1,-1):
            if (dp[n][j]==True):
                diff=min(rng-2*j,diff)
        
        return diff