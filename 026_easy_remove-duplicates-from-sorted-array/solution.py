class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        res = nums[:1]
        k = 1

        for n in nums[1:]:
            if n == res[-1]:
                continue
            res.append(n)
            k += 1
        
        nums[:k] = res

        return k