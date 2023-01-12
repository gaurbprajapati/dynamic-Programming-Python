

'''
Given an integer n, return the least number of perfect square numbers that sum to n.
A perfect square is an integer that is the square of an integer; in other words, it is the product of some integer with itself. For example, 1, 4, 9, and 16 are perfect squares while 3 and 11 are not.

'''


import math

global intmax

intmax = math.inf-1


def coins_change2(coins, s):
    n = len(coins)
    dp = [[0]*(s+1) for i in range(n+1)]
    for i in range(n+1):
        for j in range(s+1):
            if (j == 0):
                dp[i][j] = 0
            if (i == 0):
                dp[i][j] = intmax
            if(i == 1):
                if(j % coins[i-1] == 0):
                    dp[i][j] = j//coins[i-1]
                else:
                    dp[i][j] = intmax
        dp[0][0] = 0

    for i in range(1, n+1):
        for j in range(1, s+1):
            if (coins[i-1] <= j):
                dp[i][j] = min(dp[i-1][j], 1+dp[i][j-coins[i-1]])
            else:
                dp[i][j] = dp[i-1][j]

    if (dp[n][s] != intmax):
        return dp[n][s]
    else:
        return -1


n = 25

arr = []

i = 1
while(i**2 < n+1):
    arr.append(i**2)
    i += 1

print(coins_change2(arr, n))


'''

#include <bits/stdc++.h>
using namespace std;
#define INF INT_MAX-1
class Solution {
public:
    int numSquares(int sum) {
    vector<int> coins;
    int i =1;
    while(pow(i,2)<sum+1){
        coins.push_back(pow(i,2));
        i++;
    }
    int n=coins.size();
    int t[n + 1][sum + 1];
	// initialization
	for (int i = 0; i <= n; i++) {
		for (int j = 0; j <= sum; j++) {
			if (j == 0)
				t[i][j] = 0;
			if (i == 0)
				t[i][j] = INF;
			if (i == 1) {
				if (j % coins[i - 1] == 0)
					t[i][j] = j / coins[i - 1];
				else
					t[i][j] = INF;
			}
		}
	}
	t[0][0] = 0;

	for (int i = 1; i <= n; i++)
		for (int j = 1; j <= sum; j++)
			if (coins[i - 1] <= j)
				t[i][j] = min(t[i - 1][j], 1 + t[i][j - coins[i - 1]]);
			else
				t[i][j] = t[i - 1][j];

	if(t[n][sum]==INF) {
        return -1;
    }else{
        return t[n][sum];
    }



    }
};

'''
