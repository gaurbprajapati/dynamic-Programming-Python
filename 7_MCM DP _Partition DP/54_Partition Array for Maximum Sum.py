class Solution:
    def memo(self, ind, arr, n, k, dp):
        if (ind == n):
            return 0

        if (dp[ind] != -1):
            return dp[ind]

        ln = 0
        maxAns = -float('inf')
        mini = -float('inf')

        for j in range(ind, min(ind+k, n)):
            ln += 1
            mini = max(mini, arr[j])
            csum = (mini*ln)+self.memo(j+1, arr, n, k, dp)
            maxAns = max(maxAns, csum)

        dp[ind] = maxAns

        return dp[ind]

    def tabulation(self, n, arr, k):

        dp = [0]*(n+1)

        dp[n] = 0  # ini

        for ind in range(n-1, -1, -1):
            ln = 0
            maxAns = -float('inf')
            mini = -float('inf')
            for j in range(ind, min(ind+k, n)):
                ln += 1
                mini = max(mini, arr[j])
                csum = (mini*ln)+self.memo(j+1, arr, n, k, dp)
                maxAns = max(maxAns, csum)
            dp[ind] = maxAns

        return dp[0]

    def maxSumAfterPartitioning(self, arr, k: int) -> int:
        n = len(arr)
        dp = [-1 for i in range(n+1)]

        # return self.memo(0, arr,n , k , dp)
        return self.tabulation(n, arr, k)


arr = [1, 15, 7, 9, 2, 5, 10]
k = 3
ob = Solution()
print(ob.maxSumAfterPartitioning(arr, k))
