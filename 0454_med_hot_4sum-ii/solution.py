from collections import defaultdict
from typing import List

class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        records = defaultdict(int)

        n = len(nums1)

        for a in nums1:
            for b in nums2:
                records[a+b] += 1

        result = 0

        for c in nums3:
            for d in nums4:
                result += records[-(c + d)]
        
        return result