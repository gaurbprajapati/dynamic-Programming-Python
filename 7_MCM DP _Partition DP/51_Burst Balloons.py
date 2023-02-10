class Solution:
    def memo(self, arr, i, j, dp):
        if (i > j):
            return 0
        if dp[i][j] != -1:
            return dp[i][j]
        maxi = -float('inf')
        for k in range(i, j+1):
            ans = self.memo(arr, i, k-1, dp)+self.memo(arr, k +
                                                       1, j, dp)+(arr[i-1]*arr[k]*arr[j+1])
            maxi = max(maxi, ans)
        dp[i][j] = maxi
        return dp[i][j]

    def tabulation(self, n, arr):
        dp = [[0 for i in range(n+2)] for j in range(n+2)]
        for i in range(n, 0, -1):
            for j in range(1, n+1):
                if (i > j):
                    continue
                maxi = -float('inf')
                for k in range(i, j+1):
                    ans = dp[i][k-1]+dp[k+1][j]+(arr[i-1]*arr[k]*arr[j+1])
                    maxi = max(maxi, ans)
                dp[i][j] = maxi
        return dp[1][n]

    def maxCoins(self, arr) -> int:
        N = len(arr)
        arr.insert(0, 1)
        arr.append(1)

        i = 1
        j = N
        dp = [[-1 for i in range(N+1)] for j in range(N+1)]
        # return self.memo(arr,i,j,dp)

        return self.tabulation(N, arr)


nums = [3, 1, 5, 8]

print(Solution().maxCoins(nums))
