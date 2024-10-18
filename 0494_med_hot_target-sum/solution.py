from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)

        # 此时没有方案
        if abs(target) - total > 0:
            return 0
        
        # 此时没有方案
        if (target + total) % 2 == 1:
            return 0
        
        bag_size = (target + total) // 2

        dp = [[0] * (bag_size + 1) for _ in range(len(nums))]

        # 初始化最上行
        if nums[0] <= bag_size:
            dp[0][nums[0]] = 1

        # 初始化最左列，最左列其他数值在递推公式中就完成了赋值
        dp[0][0] = 1

        num_zero = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                num_zero += 1
            dp[i][0] = 2 ** num_zero

        for i in range(1, len(nums)):
            for j in range(0, bag_size + 1):
                if nums[i] > j:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i-1][j - nums[i]]

        return dp[-1][bag_size]


        