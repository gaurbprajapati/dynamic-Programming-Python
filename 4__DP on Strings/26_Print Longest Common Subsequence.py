

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
    return dp


def printing_lcs(s1, s2, n, m):
    dp = LCS(s1, s2, n, m)

    i = n
    j = m
    ans = ""
    while(i > 0 and j > 0):
        if (s1[i-1] == s2[j-1]):
            ans += s1[i-1]
            i -= 1
            j -= 1
        elif (dp[i][j-1] > dp[i-1][j]):
            j -= 1
        else:
            i -= 1
    return ans[::-1]


X = "AGGTAB"
Y = "GXTXAYB"
n = len(X)
m = len(Y)
print(printing_lcs(X, Y, n, m))
