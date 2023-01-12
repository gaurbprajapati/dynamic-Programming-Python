

# same as the last problem number 4

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums)

        return max(self.solve(nums[1:]), self.solve(nums[:-1]))

    def solve(self, a):
        prev2 = 0
        prev = a[0]
        for i in range(1, len(a)):
            pick = a[i]
            if (i > 1):
                pick += prev2
            notpick = 0+prev
            curr = max(pick, notpick)
            prev2 = prev
            prev = curr
        return prev
