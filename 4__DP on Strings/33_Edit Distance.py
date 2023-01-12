class Solution:
    def memo(self, s1, s2, i, j, dp):

        if (j == 0):
            return i
        if (i == 0):
            return j

        if (dp[i][j] != -1):
            return dp[i][j]

        if (s1[i-1] == s2[j-1]):
            dp[i][j] = 0+self.memo(s1, s2, i-1, j-1, dp)
        else:
            dp[i][j] = 1+min(self.memo(s1, s2, i-1, j-1, dp),
                             self.memo(s1, s2, i, j-1, dp), self.memo(s1, s2, i-1, j, dp))

        return dp[i][j]

    def tabulation(self, s1, s2, n, m):
        dp = [[0 for i in range(m+1)] for j in range(n+1)]

        for i in range(n+1):
            for j in range(m+1):
                if j == 0:
                    dp[i][j] = i
                    continue
                if i == 0:
                    dp[i][j] = j
                    continue
                if (s1[i-1] == s2[j-1]):
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = 1+min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])

        return dp[n][m]

    def spaceOptimization(self, s1, s2, n, m):
        prev = [0 for i in range(m+1)]

        for i in range(n+1):
            curr = [0 for i in range(m+1)]
            for j in range(m+1):
                if j == 0:
                    curr[j] = i
                    continue
                if i == 0:
                    curr[j] = j
                    continue
                if (s1[i-1] == s2[j-1]):
                    curr[j] = prev[j-1]
                else:
                    curr[j] = 1+min(prev[j-1], prev[j], curr[j-1])
            prev = curr

        return prev[m]

    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)
        dp = [[-1 for i in range(m+1)] for j in range(n+1)]
        print(self.memo(word1, word2, n, m, dp))
        print(self.tabulation(word1, word2, n, m))
        print(self.spaceOptimization(word1, word2, n, m))


word1 = "horse"
word2 = "ros"

ob = Solution()
ob.minDistance(word1, word2)
