# https://practice.geeksforgeeks.org/problems/longest-common-substring1452/1?utm_source=gfg&utm_medium=article&utm_campaign=bottom_sticky_on_article

def LCS(s1, s2, n, m):
    dp = [[0]*(m+1) for i in range(n+1)]
    ans = 0
    for i in range(n+1):
        for j in range(m+1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif (s1[i-1] == s2[j-1]):
                dp[i][j] = 1+dp[i-1][j-1]
                ans = max(ans, dp[i][j])
            else:
                dp[i][j] = 0
    return ans


s1 = "ABCDGH"
s2 = "ACDGHR"
n = 6
m = 6

print(LCS(s1, s2, len(s1), len(s2)))
