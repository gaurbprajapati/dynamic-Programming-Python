

# https://leetcode.com/problems/longest-palindromic-substring/description/


class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False]*n for i in range(n)]
        ans = ""
        for g in range(n):
            i = 0
            for j in range(g, n):
                if(g == 0):  # initilization 1
                    dp[i][j] = True
                elif (g == 1):  # initilization 2
                    if (s[i] == s[j]):
                        dp[i][j] = True
                    else:
                        dp[i][j] = False
                else:
                    if (s[i] == s[j] and dp[i+1][j-1] == True):
                        dp[i][j] = True
                    else:
                        dp[i][j] = False
                if dp[i][j] == True:
                    ans = s[i:j+1]
                i += 1
        return ans


ob = Solution()
output = ob.longestPalindrome("heeel")
print(output)

'''

# java correct solution

class Solution {
    public String longestPalindrome(String s) {
        int n = s.length()
        boolean[][] dp = new boolean[n][n]
        var ans = ""
        for(int g=0
            g < n
            g++){
            for(int i=0, j=g
                j < n
                i++, j++){
                if(g == 0){
                    dp[i][j] = true
                }else if (g == 1){
                    if (s.charAt(i) == s.charAt(j)){
                        dp[i][j] = true
                    }else{
                        dp[i][j] = false
                    }

                }else{
                    if (s.charAt(i) == s.charAt(j) & & dp[i+1][j-1] == true){
                        dp[i][j] = true
                    }else{
                        dp[i][j] = false
                    }
                }
                if (dp[i][j] == true){
                    ans = s.substring(i, j+1)
                }
            }
        }
        return ans
    }
}

'''


'''
from numpy import matrix

def LCS(s1, s2, n, m):
    dp = [[0]*(m+1) for i in range(n+1)]
    for i in range(n+1):
        for j in range(m+1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif (s1[i-1] == s2[j-1]):
                dp[i][j] = 1+dp[i-1][j-1]
            else:
                dp[i][j] = 0
    return dp


s1 = "aaa"
s2 = "dabab"


# aba or bab -->> 3

dp = LCS(s1, s1[::-1], len(s1), len(s1))
print(matrix(dp))

# cur_index = [-1, -1]
# cur_max = -1
# for i in range(len(s1)+1):
#     for j in range(len(s1)+1):
#         if dp[i][j] > cur_max:
#             cur_max = dp[i][j]
#             cur_index = [i, j]


# print(cur_index, cur_max)

# ans = ""
# row = cur_index[0]
# col = cur_index[1]
# while(row > 0 and col > 0):
#     if dp[row][col] <= 0:
#         break
#     ans += s1[row-1]
#     col -= 1
#     row -= 1

# def checkPal(ans):
#     if ans==ans[::-1]:
#         return True
#     return False

# def palmaker(ans,ind):
#     if ind==len(ans):
#         return
#     if checkPal(ans):
#         return ans
#     return palmaker(ans[1:],ind+1)


# if ans==ans[::-1]:
#     print(ans)


'''
