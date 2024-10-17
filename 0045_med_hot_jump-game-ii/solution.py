from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)

        if n <= 1:
            return 0
        
        curDistance = 0   # 当前覆盖最远距离下标
        ans = 0           # 记录走的最大步数
        nextDistance = 0  # 下一步覆盖最远距离下标

        for i in range(n):
            nextDistance = max(nextDistance, i + nums[i]) # 更新下一步覆盖最远距离下标
            if i == curDistance:           # 遇到当前覆盖最远距离下标
                ans += 1                   # 需要走下一步
                curDistance = nextDistance # 更新当前覆盖最远距离下标（相当于加油了）
                if nextDistance >= n - 1:  # 当前覆盖最远距到达集合终点，不用做ans++操作了，直接结束
                    break
        return ans
            