# User function Template for python3

class Solution:
    def memo(self, arr, i, j, dp):
        if (i == j):
            return 0
        if dp[i][j] != -1:
            return dp[i][j]

        mini = float('inf')

        for k in range(i, j):
            ans = self.memo(arr, i, k, dp)+self.memo(arr, k +
                                                     1, j, dp)+arr[i-1]*arr[k]*arr[j]
            mini = min(mini, ans)
        dp[i][j] = mini
        return dp[i][j]

    def tabulation(self, arr, n):
        dp = [[0 for i in range(n+1)] for j in range(n+1)]

        for i in range(n-1, 0, -1):
            for j in range(i+1, n):
                mini = float('inf')
                for k in range(i, j):
                    ans = dp[i][k] + dp[k+1][j] + arr[i-1]*arr[k]*arr[j]
                    mini = min(mini, ans)
                dp[i][j] = mini

        return dp[1][n-1]

    def matrixMultiplication(self, N, arr):
        i = 1
        j = N-1
        dp = [[-1 for i in range(N+1)] for j in range(N+1)]
        # return self.memo(arr,i,j,dp)
        return self.tabulation(arr, N)


# {
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        arr = input().split()
        for i in range(N):
            arr[i] = int(arr[i])

        ob = Solution()
        print(ob.matrixMultiplication(N, arr))
# } Driver Code Ends
