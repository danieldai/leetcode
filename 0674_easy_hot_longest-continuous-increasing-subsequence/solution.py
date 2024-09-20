from typing import List


class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        max_count = 1
        count = 1
        prev = nums[0]

        for num in nums[1:]:
            if num > prev:
                count += 1
                print(count)
                max_count = max(max_count, count)
            else:
                count = 1
            prev = num
        
        return max_count
    

# DP
class Solution2:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        result = 1
        dp = [1] * len(nums)
        for i in range(len(nums)-1):
            if nums[i+1] > nums[i]: #连续记录
                dp[i+1] = dp[i] + 1
            result = max(result, dp[i+1])
        return result