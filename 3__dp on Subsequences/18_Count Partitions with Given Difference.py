class Solution:

    def solveMemo(self, ind, arr, target, dp):

        # this base is fail when the elements in the array is 0
        # example [0,0,1]
        # if (target == 0):
        #     return 1
        # if (ind == 0):
        #     if arr[ind] == target:
        #         return 1
        #     else:
        #         return 0
        # ---------------------------------------------------

        # this is the base case when the elemenets of the array is 0<=
        # example [0,0,1]
        if (ind == 0):
            if (target == 0 and arr[0] == 0):
                return 2
            if (target == 0 or target == arr[0]):
                return 1
        else:
            return 0
# ------------------------------------
        if (dp[ind][target] != -1):
            return dp[ind][target]
        notpick = self.solveMemo(ind-1, arr, target, dp)
        pick = 0
        if (target >= arr[ind]):
            pick = self.solveMemo(ind-1, arr, target-arr[ind], dp)

        dp[ind][target] = (pick + notpick)

        return dp[ind][target]

    def tabulation(self, n, arr, target, dp):
        # for i in range(n):
        #     dp[i][0] = 1
        # if(arr[0] <= target):
        #     dp[0][arr[0]] = 1

        if (arr[0] == 0):
            dp[0][0] = 2
        else:
            dp[0][0] = 1

        if (arr[0] != 0 and arr[0] <= target):
            dp[0][arr[0]] = 1

        for ind in range(1, n):
            for targ in range(0, target+1):
                notpick = dp[ind-1][targ]
                pick = 0
                if (targ >= arr[ind]):
                    pick = dp[ind-1][targ-arr[ind]]

                dp[ind][targ] = (pick + notpick)

        return dp[n-1][target]

    def spaceOptimization(self, n, arr, target):
        prev = [0 for i in range(target+1)]
        # prev[0] = True
        # if (arr[0] <= target):
        #     prev[arr[0]] = True

        if (arr[0] == 0):
            prev[0] = 2
        else:
            prev[0] = 1

        if (arr[0] != 0 and arr[0] <= target):
            prev[arr[0]] = 1

        for ind in range(1, n):
            curr = [0 for i in range(target+1)]
            for targ in range(target+1):
                notpick = prev[targ]
                pick = 0
                if (targ >= arr[ind]):
                    pick = prev[targ-arr[ind]]

                curr[targ] = (pick + notpick)
            prev = curr

        return prev[target]

    def isSubsetSum(self, n, arr, d):
        totSum = sum(arr)
        s = (totSum-d)//2
        dp = [[-1 for i in range(s + 1)] for i in range(n + 1)]
        dp2 = [[0 for i in range(s + 1)] for i in range(n + 1)]
        # return self.solve(n-1,arr,s,dp)
        # return self.tabulation(n,arr,s,dp2)
        if(totSum-d < 0):
            return 0
        if((totSum-d) % 2 == 1):
            return 0
        return self.spaceOptimization(n, arr, s)
