class Solution:
    def isallstar(self, p, i) -> bool:
        for ii in range(1, i+1):
            if (p[ii-1] != "*"):
                return False
        return True

    def memo(self, p, s, i, j, dp):
        if (i < 0 and j < 0):
            return True
        if (i < 0 and j >= 0):
            return False
        if (j < 0 and i >= 0):
            for ii in range(i+1):
                if p[ii] != "*":
                    return False
            else:
                return True

        if dp[i][j] != -1:
            return dp[i][j]
        if (p[i] == s[j] or p[i] == "?"):
            dp[i][j] = self.memo(p, s, i-1, j-1, dp)

        elif (p[i] == "*"):
            dp[i][j] = (self.memo(p, s, i-1, j, dp)
                        or self.memo(p, s, i, j-1, dp))
        else:
            dp[i][j] = False
        return dp[i][j]

    def tabulation(self, p, s, n, m):
        dp = [[0 for i in range(m+1)] for j in range(n+1)]
        dp[0][0] = True
        for j in range(1, m+1):
            dp[0][j] = False

        for i in range(1, n+1):
            dp[i][0] = self.isallstar(p, i)

        for i in range(1, n+1):
            for j in range(1, m+1):
                if (p[i-1] == s[j-1] or p[i-1] == "?"):
                    dp[i][j] = dp[i-1][j-1]

                elif (p[i-1] == "*"):
                    dp[i][j] = (dp[i-1][j] or dp[i][j-1])
                else:
                    dp[i][j] = False
        return dp[n][m]

    def spaceOptimization(self, s, p, n, m):
        prev = [0 for i in range(m+1)]
        curr = [0 for i in range(m+1)]
        prev[0] = True
        for i in range(1, n+1):
            curr[0] = self.isallstar(p, i)
            for j in range(1, m+1):
                if (p[i-1] == s[j-1] or p[i-1] == "?"):
                    curr[j] = prev[j-1]
                elif (p[i-1] == "*"):
                    curr[j] = (prev[j] or curr[j-1])
                else:
                    curr[j] = False
            prev = [val for val in curr]
        return prev[m]

    def isMatch(self, s: str, p: str) -> bool:
        n = len(p)
        m = len(s)
        dp = [[-1 for i in range(m+1)] for j in range(n+1)]
        print(self.memo(p, s, n-1, m-1, dp))
        print(self.tabulation(p, s, n, m))
        print(self.spaceOptimization(s, p, n, m))


s = "cb"
p = "?a"
ob = Solution()
ob.isMatch(s="aa", p="*")
