from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return None
        
        f = 0
        ans = float('-inf')
        
        for i in range(len(nums)):
            if f > 0:
                f = f + nums[i]
            else:
                f = nums[i]
            ans = max(f, ans)
                
        return ans  