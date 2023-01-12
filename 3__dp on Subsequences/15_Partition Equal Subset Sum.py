class Solution:

    def solveMemo(self, ind, arr, target, dp):
        if (target == 0):
            return True
        if (ind == 0):
            return arr[ind] == target

        if (dp[ind][target] != -1):
            return dp[ind][target]
        notpick = self.solveMemo(ind-1, arr, target, dp)
        pick = False
        if (target >= arr[ind]):
            pick = self.solveMemo(ind-1, arr, target-arr[ind], dp)

        dp[ind][target] = (pick or notpick)

        return dp[ind][target]

    def tabulation(self, n, arr, target, dp):
        for i in range(n):
            dp[i][0] = True
        if(arr[0] <= target):
            dp[0][arr[0]] = True

        for ind in range(1, n):
            for targ in range(1, target+1):
                notpick = dp[ind-1][targ]
                pick = False
                if (targ >= arr[ind]):
                    pick = dp[ind-1][targ-arr[ind]]

                dp[ind][targ] = (pick or notpick)

        return dp[n-1][target]

    def spaceOptimization(self, n, arr, target):
        prev = [False for i in range(target+1)]
        prev[0] = True
        if (arr[0] <= target):
            prev[arr[0]] = True

        for ind in range(1, n):
            curr = [False for i in range(target+1)]
            for targ in range(1, target+1):
                notpick = prev[targ]
                pick = False
                if (targ >= arr[ind]):
                    pick = prev[targ-arr[ind]]

                curr[targ] = (pick or notpick)
            prev = curr

        return prev[target]

    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        s = sum(nums)
        dp = [[-1 for i in range(s//2 + 1)] for i in range(n + 1)]
        dp2 = [[False for i in range(s//2 + 1)] for i in range(n + 1)]
        if s % 2 != 0:
            return False

        return self.solveMemo(n-1, nums, s//2, dp)
        # return self.tabulation(n, nums, s//2,dp2)
        # return self.spaceOptimization(n,nums,s//2)
