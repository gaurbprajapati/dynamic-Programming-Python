class Solution {
    public int findTargetSumWays(int[] nums, int target) {
          int n = nums.length;
          int arrsum = 0;
          for(int i=0;i<n;i++){
              arrsum+=nums[i];
          }
          
          if( arrsum < target || arrsum + target < 0 ||  (arrsum  + target) %2 != 0 )
           return 0;
          
          int sum = (target+arrsum)/2;
          
          int[][] dp = new int[n+1][sum+1];
          
          for(int i=0;i<n+1;i++){
             for(int j=0;j<sum+1;j++){
                 if(i==0)
                 dp[i][j] = 0;
                 if(j==0)
                 dp[i][j] = 1;
             }
         }
          
          for(int i=1;i<n+1;i++){
              for(int j=0;j<sum+1;j++){ // usually we start j=1 but here to counter zero we initialize it with j=0
                  if(nums[i-1]<=j){
                      dp[i][j] = (dp[i-1][j-nums[i-1]]) + (dp[i-1][j]);
                  }else{
                      dp[i][j] = dp[i-1][j];
                  }
              }
          }
          
          return dp[n][sum];
      }
  }