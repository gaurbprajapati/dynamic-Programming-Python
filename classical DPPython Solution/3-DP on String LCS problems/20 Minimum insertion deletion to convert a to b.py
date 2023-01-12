

def LCS(s1, s2, n, m):
    dp = [[0]*(m+1) for i in range(n+1)]
    for i in range(n+1):
        for j in range(m+1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif (s1[i-1] == s2[j-1]):
                dp[i][j] = 1+dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[n][m]


def minOperations(s1, s2):
    lcs_len = LCS(s1, s2, len(s1), len(s2))

    min_deletion = len(s1)-lcs_len
    min_insertion = len(s2)-lcs_len
    return min_deletion+min_insertion


str1 = "heap"
str2 = "pea"
print(minOperations(str1, str2))
