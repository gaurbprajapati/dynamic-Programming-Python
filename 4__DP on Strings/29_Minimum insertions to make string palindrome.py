class Solution:

    def tabulation(self, s1, s2, n, m):
        dp = [[0]*(m+1) for i in range(n+1)]
        for i in range(n+1):
            for j in range(m+1):
                if i == 0 or j == 0:
                    dp[i][j] = 0
                elif (s1[i-1] == s2[j-1]):
                    dp[i][j] = 1+dp[i-1][j-1]
                else:
                    dp[i][j] = 0+max(dp[i-1][j], dp[i][j-1])
        return dp[n][m]

    def spaceOptimization(self, s1, s2, n, m):
        prev = [0 for i in range(m+1)]
        curr = [0 for j in range(m+1)]
        for i in range(1, n+1):
            # curr = [0 for j in range(m+1)]
            for j in range(1, m+1):
                if (s1[i-1] == s2[j-1]):
                    curr[j] = 1+prev[j-1]
                else:
                    curr[j] = 0+max(prev[j], curr[j-1])
            prev = [val for val in curr]
            # prev = curr

        return prev[m]

    def LongestPalindromicSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)
        dp = [[-1]*(1001) for i in range(1001)]
        # return self.memo(text1,text2,n-1,m-1,dp)
        # return self.tabulation(text1,text2,n,m)
        return self.spaceOptimization(text1, text2, n, m)


text1 = "abcaa"

n = len(text1)
ob = Solution()

print(n-ob.spaceOptimization(text1, text1[::-1], n, n))
print(n-ob.tabulation(text1, text1[::-1], n, n))
