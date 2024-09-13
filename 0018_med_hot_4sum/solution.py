from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums = sorted(nums)
        n = len(nums)
        result = []

        for k in range(n):
            if nums[k] >= 0 and nums[k] > target:
                break

            if k > 0 and nums[k] == nums[k - 1]:
                continue

            for i in range(k + 1, n):
                if nums[k] + nums[i] > target and nums[k] + nums[i] >= 0:
                    break

                if i > k + 1 and nums[i] == nums[i - 1]:
                    continue

                left = i + 1
                right = n - 1

                while left < right:
                    s = nums[k] + nums[i] + nums[left] + nums[right]
                    if s < target:
                        left += 1
                    elif s > target:
                        right -= 1
                    else:    
                        result.append([nums[k], nums[i], nums[left], nums[right]])
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while left < right and nums[right - 1] ==  nums[right]:
                            right -= 1

                        left += 1
                        right -= 1
            
        return result
                    
                    



