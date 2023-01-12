class Solution:
    def isSubsetSum(self, n, arr, sum):
        dp = [[False for i in range(sum + 1)] for i in range(n + 1)]

        # for i in range (n+1):
        #     for j in range (sum+1):
        #         if i==0:
        #             dp[i][j]=False
        #         if j==0:
        #             dp[i][j]==True

        for i in range(n+1):
            for j in range(sum+1):
                if i == 0 and j == 0:
                    dp[i][j] = 1
                elif i == 0:
                    dp[i][j] = 0
                elif j == 0:
                    dp[i][j] = 1

                elif (arr[i-1] <= j):
                    dp[i][j] = (dp[i-1][j] + dp[i-1][j-arr[i-1]])

                elif (arr[i-1] > j):
                    dp[i][j] = dp[i-1][j]

        return dp[n][sum]
