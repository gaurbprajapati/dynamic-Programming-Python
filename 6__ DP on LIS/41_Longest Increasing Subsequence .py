class Solution:
    def memo(self, ind, prev, arr, n, dp):
        if ind == n:
            return 0
        if dp[ind][prev+1] != -1:
            return dp[ind][prev+1]
        ln = self.LIS(ind+1, prev, arr, n, dp)
        if (prev == -1 or arr[prev] < arr[ind]):
            ln = max(ln, 1+self.LIS(ind+1, ind, arr, n, dp))
        dp[ind][prev+1] = ln

        return ln

    def tabulation(self, arr, n):

        dp = [[0 for i in range(n+1)] for j in range(n+1)]

        for ind in range(n-1, -1, -1):
            for prev in range(n-1, -2, -1):
                nottake = dp[ind+1][prev+1]
                take = 0
                if (prev == -1 or arr[prev] < arr[ind]):
                    take = 1+dp[ind+1][ind+1]
                dp[ind][prev+1] = max(take, nottake)

        return dp[0][0]

    def spaceOptimization(self, arr, n):
        ahead = [0 for i in range(n+1)]
        curr = [0 for i in range(n+1)]

        for ind in range(n-1, -1, -1):
            for prev in range(n-1, -2, -1):
                nottake = 0+ahead[prev+1]
                take = 0
                if (prev == -1 or arr[prev] < arr[ind]):
                    take = 1+ahead[ind+1]
                curr[prev+1] = max(take, nottake)
            ahead = curr

        return ahead[0]

    def longestIncreasingSubsequence(self, arr, n):
        dp = [1]*(n+1)

        for ind in range(0, n):
            for prev in range(0, ind):
                if (arr[prev] < arr[ind]):
                    dp[ind] = max(dp[ind], 1+dp[prev])

        return max(dp)

    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[-1]*(n+1) for i in range(n+2)]
        # return self.memo(0,-1,nums,len(nums),dp)
        # return self.tabulation(nums,len(nums))
        # return self.spaceOptimization(nums,len(nums))

        return self.longestIncreasingSubsequence(nums, len(nums))
