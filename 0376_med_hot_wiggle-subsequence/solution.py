from typing import List


class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return n
        
        cur_diff = 0 # 当前一对差值
        pre_diff = 0 # 前一对差值
        result = 1 # // 记录峰值个数，序列默认序列最右边有一个峰值

        for i in range(n - 1):
            cur_diff = nums[i + 1] - nums[i]
            # 出现峰值
            if (pre_diff <= 0 and cur_diff > 0) or (pre_diff >= 0 and cur_diff < 0):
                result += 1
                pre_diff = cur_diff

        return result 

# DP
class Solution2:
    def wiggleMaxLength(self, nums):
        dp = [[0, 0] for _ in range(len(nums))]  # 创建二维dp数组，用于记录摆动序列的最大长度
        dp[0][0] = dp[0][1] = 1  # 初始条件，序列中的第一个元素默认为峰值，最小长度为1
        for i in range(1, len(nums)):
            dp[i][0] = dp[i][1] = 1  # 初始化当前位置的dp值为1
            for j in range(i):
                if nums[j] > nums[i]:
                    dp[i][1] = max(dp[i][1], dp[j][0] + 1)  # 如果前一个数比当前数大，可以形成一个上升峰值，更新dp[i][1]
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i][0] = max(dp[i][0], dp[j][1] + 1)  # 如果前一个数比当前数小，可以形成一个下降峰值，更新dp[i][0]
        return max(dp[-1][0], dp[-1][1])  # 返回最大的摆动序列长度