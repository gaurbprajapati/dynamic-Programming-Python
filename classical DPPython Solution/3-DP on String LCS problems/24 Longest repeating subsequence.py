# https://practice.geeksforgeeks.org/problems/longest-repeating-subsequence2004/1?utm_source=gfg&utm_medium=article&utm_campaign=bottom_sticky_on_article

def LCS(s1, s2, n, m):
    dp = [[0]*(m+1) for i in range(n+1)]
    for i in range(n+1):
        for j in range(m+1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif (s1[i-1] == s2[j-1] and i != j):
                dp[i][j] = 1+dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[n][m]


def longestRepeatingSubsequenc(str, n):
    return LCS(str, str, n, n)


str = "aabb"
print("The length of the largest subsequence that repeats itself is : ",
      longestRepeatingSubsequenc(str, len(str)))
