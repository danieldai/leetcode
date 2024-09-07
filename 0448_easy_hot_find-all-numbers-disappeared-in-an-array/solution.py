from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        used = set(nums)

        return [n for n in range(1, len(nums) + 1) if n not in used]
    


class Solution2:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:

        for n in nums:
            nums[abs(n)-1] = -abs(nums[abs(n)-1])
        
        return [i for i in range(1, len(nums) + 1) if nums[i-1] > 0]