class Solution:
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

        return dp

    def solve(self, A):
        n = len(A)
        s = sum(A)
        dp2 = [[False for i in range(s + 1)] for i in range(n + 1)]
        dp = self.tabulation(n, A, s, dp2)
        ans = 100
        for i in range(s//2, -1, -1):
            if (dp[n-1][i] == True):
                ans = min(ans, s-2*i)
        return ans


A = [1, 6, 11, 5]
k
ob = Solution()
print(ob.solve(A))
