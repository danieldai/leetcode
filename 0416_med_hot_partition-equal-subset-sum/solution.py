from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        total = sum(nums)

        if total % 2 == 1:
            return False
        
        target = total // 2

        dp = [0] * (target + 1)

        for i in range(len(nums)):
            for j in range(target, nums[i] -1 , -1):
                dp[j] = max(dp[j], dp[j - nums[i]] + nums[i])

        return dp[target] == target


        