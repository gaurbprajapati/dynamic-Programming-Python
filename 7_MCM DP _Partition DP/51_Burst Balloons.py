class Solution:
    def memo(self, arr, i, j, dp):
        if (i > j):
            return 0
        if dp[i][j] != -1:
            return dp[i][j]

        mini = -float('inf')

        for k in range(i, j+1):
            ans = self.memo(arr, i, k-1, dp)+self.memo(arr, k +
                                                       1, j, dp)+(arr[i-1]*arr[k]*arr[j+1])
            mini = max(mini, ans)
        dp[i][j] = mini
        return dp[i][j]

    def maxCoins(self, arr: List[int]) -> int:

        arr.insert(0, 1)
        arr.append(1)
        N = len(arr)-2
        i = 1
        j = N
        dp = [[-1 for i in range(N+1)] for j in range(N+1)]
        return self.memo(arr, i, j, dp)
