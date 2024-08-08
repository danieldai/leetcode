from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return None
        
        f = nums[0]
        ans = nums[0]
        
        
        for i in range(1, len(nums)):
            if f > 0:
                f = f + nums[i]
            else:
                f = nums[i]
            ans = max(f, ans)
                
        return ans  