class Solution:
    def maxProfit(self, prices) -> int:
        ans = 0
        mini = prices[0]
        for i in range(1, len(prices)):
            profit = prices[i]-mini
            ans = max(ans, profit)
            mini = min(mini, prices[i])

        return ans if ans > 0 else 0


prices = [7, 1, 5, 3, 6, 4]
ob = Solution()
print(ob.maxProfit(prices))
