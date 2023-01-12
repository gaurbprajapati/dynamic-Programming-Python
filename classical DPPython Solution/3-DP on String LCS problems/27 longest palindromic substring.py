

class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False]*n for i in range(n)]
        ans = 0
        for g in range(n):
            i = 0
            for j in range(g, n):
                if(g == 0):
                    dp[i][j] = True
                elif (g == 1):
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
                    ans = g+1
                i += 1
        return ans


ob = Solution()
output = ob.longestPalindrome("haabbaam")
print(output)
'''

class Solution {
    public int countSubstrings(String s) {
        int n = s.length()
        boolean[][] dp = new boolean[n][n]
        int ans = 0
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
                    ans = g+1
                }
            }
        }
        return ans
    }
}

        '''
