package Python

Solution.problem_on_LCS;

public class Solution {

    public  static int lcs(int x, int y, String s1, String s2)
    {
            char[] X=s1.toCharArray(); 
           char[] Y=s2.toCharArray(); 
        int[][] dp = new int[x+1][y+1];
            for(int i=0;i<x + 1;i++){
            for(int j=0;j<y + 1;j++){
                   if (i==0 || j==0){
                       dp[i][j]=0;
                   }
                   else if  (X[i-1]==Y[j-1]){
                       dp[i][j]=1+dp[i-1][j-1];
                   }
                   else{
                       dp[i][j]=Math.max(dp[i-1][j],dp[i][j-1]);
                   }
                          
            
            }
                         
                
            }
            return dp[x][y];

    }

    public int longestCommonSubsequence(String text1, String text2) {
        
        int x=text1.length();
        int y=text2.length();

        return lcs(x,y,text1,text2);
    }
}{

}
