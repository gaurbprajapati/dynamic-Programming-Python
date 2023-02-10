class Solution:

    def isPal(self, s):
        return s[::-1] == s

    def memo(self, ind, s, dp, n):
        if(ind == n):
            return 0

        if (dp[ind] != -1):
            return dp[ind]

        temp = ""
        minAns = float('inf')
        for j in range(ind, n):
            temp += s[j]
            if self.isPal(temp):
                cost = 1+self.memo(j+1, s, dp, n)
                minAns = min(minAns, cost)
        dp[ind] = minAns

        return dp[ind]

    def tabulation(self, s, n):
        dp = [0 for i in range(n+1)]

        dp[n] = 0

        for ind in range(n-1, -1, -1):
            temp = ""
            minAns = float('inf')
            for j in range(ind, n):
                temp += s[j]
                if self.isPal(temp):
                    cost = 1+dp[j+1]
                    minAns = min(minAns, cost)
            dp[ind] = minAns

        return dp[0]

    def minCut(self, s: str) -> int:
        n = len(s)
        dp = [-1 for i in range(n+1)]
        # return self.memo(0,s,dp,n)-1

        return self.tabulation(s, n)-1
